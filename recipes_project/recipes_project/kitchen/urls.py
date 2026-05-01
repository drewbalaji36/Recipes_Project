from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path('', views.list_recipes, name='list'),
    path('add/', views.create_recipe, name='add'),
    path('<int:pk>/edit/', views.update_recipe, name='edit'),
    path('<int:pk>/delete/', views.delete_recipe, name='delete'),
    path('safe-search/', views.safe_search_by_country, name='safe_search'),
    path('bulk-spice/', views.bulk_bump_spice_for_country, name='bulk_spice'),
]
