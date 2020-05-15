from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from django import http
from django.views.generic import DetailView, UpdateView
from django.views.generic.edit import ModelFormMixin

from apps.account.forms import UserCreationForm, AuthenticationForm
from apps.account.models import LeagueUser
from apps.league.models import Team, Competition


class UpdateProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LeagueUser
    fields = ['username', 'github_link']
    template_name = 'update_profile.html'

    def get_context_data(self, **kwargs):
        context = {}
        return super().get_context_data(**context)

    def test_func(self):
        user = LeagueUser.objects.get(pk=self.kwargs['pk'])
        return user.pk == self.request.user.pk

    def get_success_url(self):
        return reverse_lazy('account:user_detail', kwargs={'pk': self.kwargs.get('pk')})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'sign_up.html'


# We are using reverse_lazy because for all generic class-based views the urls
# are not loaded when the file is imported, so we have to use the lazy form of
# reverse to load them later when they are available.

class UserDetail(LoginRequiredMixin, DetailView):
    template_name = "account.html"
    context_object_name = 'detailuser'
    model = LeagueUser

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        return context


class Login(LoginView):
    authentication_form = AuthenticationForm
    success_url = reverse_lazy('account:login')
    redirect_field_name = 'redirect_to'


class UserParticipations(LoginRequiredMixin, generic.TemplateView):
    template_name = "participations/participate.html"

    def get_context_data(self, **kwargs):
        context = super(UserParticipations, self).get_context_data(**kwargs)
        context['teams'] = Team.objects.filter(members=self.kwargs.get('pk'))
        context['competitions'] = []
        context['duser'] = LeagueUser.objects.get(pk=self.kwargs.get('pk'))
        for team in context['teams']:
            context['competitions'].append(Competition.objects.get(pk=team.competition.pk))
        context.update(kwargs)
        return context
