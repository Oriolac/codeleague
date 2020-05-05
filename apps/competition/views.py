from django import http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView
from django.views import generic

from apps.competition.forms import CompetitionCreationForm, TeamCreationForm, TeamJoinForm
from apps.league.models import Team, Competition, Category


class CreateCompetitionView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('account:login')
    form_class = CompetitionCreationForm
    template_name = 'competition/create.html'

    def get_success_url(self):
        return reverse_lazy('league:home')
        # return reverse_lazy('competition:detail', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        competition = form.save(commit=False)
        competition.owner = self.request.user
        competition.save()
        return http.HttpResponseRedirect(self.get_success_url())

class CompetitionUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Competition
    fields = ['title', 'description']
    template_name = 'competition/competition_update_form.html'

    def get_context_data(self, **kwargs):
        context = {}
        return super().get_context_data(**context)

    def test_func(self):
        competition = Competition.objects.get(pk=self.kwargs['pk'])
        return competition.owner.pk == self.request.user.pk

    def get_success_url(self):
        return reverse_lazy('league:home')


class CompetitionDetail(LoginRequiredMixin, generic.DetailView):
    login_url = reverse_lazy('account:login')
    redirect_field_name = 'redirect_to'
    context_object_name = 'competition'
    template_name = 'competition/detail.html'
    success_url = reverse_lazy('competition:join-team')
    form_class = TeamJoinForm

    queryset = Competition.objects.all()

    def get_context_data(self, **kwargs):
        context = {}
        context['user'] = self.request.user
        context['groups'] = Team.objects.filter(competition=self.kwargs.get(self.pk_url_kwarg))
        context.update(kwargs)
        return super().get_context_data(**context)
    def get_selected_team(self):
        obj = super().get_object()
        obj.save()
        return obj
    def form_valid(self, form):
        team = Team.objects.filter(id=form.cleaned_data['name'])[0]
        team.save()
        team.members.add(self.request.user.pk)
        team.save()
        return http.HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse_lazy('competition:detail', kwargs={'pk': self.kwargs['pk']})

class CreateTeam(LoginRequiredMixin, generic.CreateView):
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

    def form_valid(self, form):
        team = form.save(commit=False)
        team.competition = Competition.objects.get(pk=self.kwargs['pk'])
        team.save()
        team.members.add(self.request.user.pk)
        team.save()
        return http.HttpResponseRedirect(self.get_success_url())


class Categories(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = 'categories/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['competitions'] = {}
        for category in context['object_list']:
            context['competitions'][category.id] = Competition.objects.filter(categories__name__contains=category.name)
        return context
