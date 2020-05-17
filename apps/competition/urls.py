from django.urls import path
from apps.competition import views
from apps.competition.apps import CompetitionConfig

app_name = 'competition'
urlpatterns = [
    path('', views.ListCompetition.as_view(), name='list'),
    path('create/', views.CreateCompetitionView.as_view(), name='createcompetition'),
    path('id/<int:pk>/', views.CompetitionDetail.as_view(), name='detail'),
    path('id/<int:pk>/edit/', views.CompetitionUpdate.as_view(), name='edit'),
    path('id/<int:pk>/delete/', views.CompetitionDelete.as_view(), name='delete'),
    path('id/<int:pk>/create-team/', views.CreateTeam.as_view(), name='create-team'),
    path('id/<int:pk>/submit-answer/', views.PublishAnswerCompetition.as_view(), name='submit-answer'),
    path('id/<int:pk>/valorate-submitions/', views.RateAnswerCompetition.as_view(), name='valorate-submitions'),

    path('search/', views.SearchCompetitions.as_view(), name="search"),
]
