from django.urls import path
from apps.category import views
from apps.competition.apps import CompetitionConfig

app_name = 'category'
urlpatterns = [
    path('', views.ListCategories.as_view(), name='listofcategories'),
    path('search/', views.SearchCategories.as_view(), name="search"),
    path('<int:pk>/', views.DetailCategory.as_view(), name="detail"),
]
