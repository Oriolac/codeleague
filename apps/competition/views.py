from django import http
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views import generic
from django.shortcuts import render
from apps.competition.forms import CompetitionCreationForm, TeamCreationForm, TeamJoinForm, TeamLeaveForm, \
    PublishAnswerForm
from apps.league.models import Team, Competition, Category, Files, Ranking

import os, boto3, datetime,random

s3 = boto3.resource('s3', aws_access_key_id=str(os.getenv('AWS_KEY')),
                    aws_secret_access_key=str(os.getenv('AWS_SECRET')))
s3_client = boto3.client('s3', aws_access_key_id=str(os.getenv('AWS_KEY')),
                         aws_secret_access_key=str(os.getenv('AWS_SECRET')))


class ListCompetition(LoginRequiredMixin, generic.ListView):
    model = Competition
    template_name = 'competition/list.html'
    context_object_name = 'competitions'
    login_url = reverse_lazy('account:login')

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.all().order_by('-data_finish_competition')


class CreateCompetitionView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('account:login')
    form_class = CompetitionCreationForm
    model = Competition
    template_name = 'competition/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('competition:detail', kwargs={'pk': kwargs.get('pk')})
        # return reverse_lazy('competition:detail', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        competition = form.save(commit=False)
        competition.owner = self.request.user
        files = self.request.FILES.getlist('files')
        competition.save()
        for file_name in files:
            datecreated = datetime.datetime.now()
            s3.Bucket(os.getenv('AWS_BUCKET')).put_object(
                Key="competition/" + str(competition.id) + "_" + str(datecreated) + "_" + str(file_name),
                Body=file_name)
            file_data = Files.create(str(file_name),
                                     "competition/" + str(competition.id) + "_" + str(datecreated) + "_" + str(
                                         file_name))
            file_data.save()
            competition.files.add(file_data)
        competition.save()
        return http.HttpResponseRedirect(self.get_success_url(pk=competition.id))


class CompetitionUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Competition
    fields = ['title', 'description']
    template_name = 'competition/competition_update_form.html'
    context_object_name = 'competition'

    def get_context_data(self, **kwargs):
        context = {}
        return super().get_context_data(**context)

    def test_func(self):
        competition = Competition.objects.get(pk=self.kwargs['pk'])
        return competition.owner.pk == self.request.user.pk

    def form_valid(self, form):
        competition = form.save()
        delete = False
        res = []
        for update_file in competition.files.all():
            if (self.request.POST.get('delete' + str(update_file.id))):
                res.append({'Key': update_file.file_bucket})
                competition.files.remove(update_file)
                update_file.delete()
                delete = True
            else:
                update_file.title = self.request.POST.get('title' + str(update_file.id))
                update_file.save()
        if delete: s3.Bucket(os.getenv('AWS_BUCKET')).delete_objects(Delete={'Objects': res})
        competition.save()
        files = self.request.FILES.getlist('files')
        for file_name in files:
            datecreated = datetime.datetime.now()
            s3.Bucket(os.getenv('AWS_BUCKET')).put_object(
                Key="competition/" + str(competition.id) + "_" + str(datecreated) + "_" + str(file_name),
                Body=file_name)
            file_data = Files.create(str(file_name),
                                     "competition/" + str(competition.id) + "_" + str(datecreated) + "_" + str(
                                         file_name))
            file_data.save()
            competition.files.add(file_data)
        competition.save()
        return http.HttpResponseRedirect(self.get_success_url(pk=competition.id))

    def get_success_url(self, **kwargs):
        return reverse_lazy('competition:detail', kwargs={'pk': kwargs.get('pk')})


class CompetitionDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Competition
    template_name = 'competition/delete.html'
    success_url = reverse_lazy('competition:list')

    def get_context_data(self, **kwargs):
        context = {}
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse_lazy('competition:list')

    def test_func(self):
        competition = Competition.objects.filter(id=self.kwargs.get(self.pk_url_kwarg))[0]
        if competition.owner != self.request.user or competition.is_competition_opened():
            return False
        return True

    def form_valid(self, form):
        if self.request.method == 'POST':
            competition = Competition.objects.filter(id=self.kwargs['pk'])[0]
            if competition.is_competition_opened() is False and competition.owner == self.request.user:
                action = self.request.POST.get('action')
                if action == 'delete':
                    competition.delete(self.request.user.pk)

                return http.HttpResponseRedirect(self.get_success_url())


class CompetitionDetail(LoginRequiredMixin, generic.DetailView, generic.CreateView):
    login_url = reverse_lazy('account:login')
    redirect_field_name = 'redirect_to'
    context_object_name = 'competition'
    template_name = 'competition/detail.html'
    success_url = reverse_lazy('competition:join-team')
    form_class = TeamJoinForm

    queryset = Competition.objects.all()

    def get_context_data(self, **kwargs):
        context = {}
        r = lambda: random.randint(0,255)
        context['data'] = [["puntuation", "table", { 'role': 'style' }]]

        context['user'] = self.request.user
        competition = Competition.objects.get(pk=self.kwargs.get('pk'))
        teams_of_competition = Team.objects.filter(competition=competition)
        context['groups'] = teams_of_competition.order_by('-ranking__score')
        context['haveTeam'] = False
        for group in context['groups']:
            print(group)
            if group.submition and len(context['data']) < 10:
                if group.ranking:
                    context['data'].append(
                        [group.name, int(group.ranking.score), 'color: #%02X%02X%02X' % (r(), r(), r())])
                else:
                    context['data'].append(
                        [group.name, 0, 'color: #%02X%02X%02X' % (r(), r(), r())])
            if context['user'] in group.members.all():
                context['haveTeam'] = True
                break
        context.update(kwargs)
        competition = Competition.objects.filter(id=self.kwargs.get(self.pk_url_kwarg))[0]
        files = competition.files.all()
        context['files'] = []
        for competition_file in files:

            context['files'].append((competition_file.title, s3_client.generate_presigned_url('get_object', Params={
                'Bucket': os.getenv('AWS_BUCKET'), 'Key': competition_file.file_bucket}, ExpiresIn=100)))
        return super().get_context_data(**context)

    def form_valid(self, form):
        competition = Competition.objects.filter(id=self.kwargs['pk'])[0]
        action = self.request.POST.get('action')
        if competition.is_inscription_opened():
            team = Team.objects.filter(id=self.request.POST.get('teamId'))[0]
            if action == 'join':
                team.members.add(self.request.user.pk)
                team.save()
            elif action == 'leave':
                team.members.remove(self.request.user.pk)
                team.save()
                if len(team.members.all()) == 0:
                    team.delete()
            return http.HttpResponseRedirect(self.get_success_url())
        return http.HttpResponseForbidden()

    def get_success_url(self):
        return reverse_lazy('competition:detail', kwargs={'pk': self.kwargs['pk']})


class CreateTeam(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    login_url = reverse_lazy('account:login')
    template_name = 'team/create.html'
    success_url = reverse_lazy('competition:create-team')
    queryset = Competition.objects.all()
    form_class = TeamCreationForm

    def get_context_data(self, **kwargs):
        context = {}

        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse_lazy('competition:detail', kwargs={'pk': self.kwargs['pk']})

    def test_func(self):
        competition = Competition.objects.filter(id=self.kwargs.get(self.pk_url_kwarg))[0]
        if competition.owner == self.request.user:
            return False
        teams = Team.objects.filter(competition=self.kwargs.get(self.pk_url_kwarg))
        for team in teams:
            if self.request.user in team.members.all():
                return False
        return True

    def form_valid(self, form):
        team = form.save(commit=False)
        team.competition = Competition.objects.get(pk=self.kwargs['pk'])
        team.save()
        team.members.add(self.request.user.pk)
        team.save()
        return http.HttpResponseRedirect(self.get_success_url())


class SearchCompetitions(LoginRequiredMixin, generic.TemplateView):
    context_object_name = 'context'
    template_name = 'search/list.html'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q-comp')
        competitions = Competition.objects.filter(title__contains=query).union(
            Competition.objects.filter(description__contains=query))
        context = {'query': query, 'competitions': competitions}
        return context


class PublishAnswerCompetition(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    login_url = reverse_lazy('account:login')
    redirect_field_name = 'redirect_to'
    context_object_name = 'competition'
    template_name = 'competition/submit.html'
    success_url = reverse_lazy('competition:submit-answer')
    form_class = PublishAnswerForm

    queryset = Competition.objects.all()

    def get_team(self):
        competition = Competition.objects.get(id=self.kwargs['pk'])
        competition_groups = Team.objects.filter(competition=competition)

        for group in competition_groups:
            if self.request.user in group.members.all():
                return group
        return None

    def get_context_data(self, **kwargs):

        context = {}
        context['team'] = self.get_team()
        return super().get_context_data(**context)

    def test_func(self):

        competition = Competition.objects.get(id=self.kwargs['pk'])

        return competition.is_competition_opened() and self.get_team()

    def form_valid(self, form):
        team = self.get_team()
        submit = form.save()
        res = []
        delete = False
        if team.submition:
            for update_file in team.submition.files.all():
                if (self.request.POST.get('delete' + str(update_file.id))):
                    res.append({'Key': update_file.file_bucket})
                    team.submition.files.remove(update_file)
                    update_file.delete()
                    delete = True
                else:
                    submit.files.add(update_file)
        if delete: s3.Bucket(os.getenv('AWS_BUCKET')).delete_objects(Delete={'Objects': res})
        submit.team_id = team.id
        submit.save()
        team.submition = submit
        team.save()
        files = self.request.FILES.getlist('files')
        for file_name in files:
            datecreated = datetime.datetime.now()
            s3.Bucket(os.getenv('AWS_BUCKET')).put_object(
                Key="submit/" + str(submit.id) + "_" + str(datecreated) + "_" + str(file_name), Body=file_name)
            file_data = Files.create(str(file_name),
                                     "submit/" + str(submit.id) + "_" + str(datecreated) + "_" + str(file_name))
            file_data.save()
            submit.files.add(file_data)
        submit.save()
        return http.HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('competition:detail', kwargs={'pk': self.kwargs['pk']})



class CompetitionFinish(LoginRequiredMixin, UserPassesTestMixin, generic.TemplateView):
    login_url = reverse_lazy('account:login')
    template_name = 'team/list.html'

    def test_func(self):
        competition = Competition.objects.get(pk=self.kwargs['pk'])
        return competition.owner.pk == self.request.user.pk

    def get_context_data(self, **kwargs):
        context = {'user': self.request.user}
        teams = Team.objects.filter(competition=self.kwargs.get('pk'))
        context['teams'] = teams
        context.update(kwargs)
        return super().get_context_data(**context)


class RateAnswerCompetition(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    context_object_name = 'competition'
    template_name = 'competition/rate.html'
    queryset = Competition.objects.all()
    fields = []

    def test_func(self):
        competition = Competition.objects.get(pk=self.kwargs['pk'])
        return competition.owner.pk == self.request.user.pk and not competition.finalized

    def get_context_data(self, **kwargs):
        context = {}
        context['groups'] = Team.objects.filter(competition=self.kwargs['pk'], submition__isnull=False)
        context['files'] = []
        for team in context['groups']:
            for submit_file in team.submition.files.all():
                context['files'].append((team.id, submit_file.title, s3_client.generate_presigned_url('get_object',
                                                                                                      Params={
                                                                                                          'Bucket': os.getenv(
                                                                                                              'AWS_BUCKET'),
                                                                                                          'Key': submit_file.file_bucket},
                                                                                                      ExpiresIn=100)))
        return super().get_context_data(**context)

    def form_valid(self, form):
        print(self.request.POST)
        competition = Competition.objects.get(pk=self.kwargs['pk'])
        teams = Team.objects.filter(competition=competition)
        for team in teams:
            if team.submition: 
                team.ranking = Ranking.create(self.request.POST.get("puntuation" + str(team.id)))
                team.ranking.save()
                print(team.ranking)
                team.save()
            else:
                team.ranking = Ranking.create(0)
                team.ranking.save()
                team.save()
        competition.finalized = True
        competition.save()
        return http.HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('competition:detail', kwargs={'pk': self.kwargs['pk']})
