from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path('', views.list_recipes, name='list'),
    path('add/', views.create_recipe, name='add'),
    path('<int:pk>/edit/', views.update_recipe, name='edit'),
    path('<int:pk>/delete/', views.delete_recipe, name='delete'),
]
