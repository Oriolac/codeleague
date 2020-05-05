from django.urls import path
from apps.category import views
from apps.competition.apps import CompetitionConfig

app_name = 'category'
urlpatterns = [
    path('', views.ListCategories.as_view(), name='listofcategories'),
]
