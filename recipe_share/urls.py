from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('change-password/', views.change_password, name='change-password'),
    path('contact/', views.contact, name='contact'),
    path('view-recipe/<int:recipe_id>/', views.view_recipe, name="view-recipe"),
    path('create-recipe/', views.create_recipe, name="create-recipe"),
    path('recipes/<str:filter>/', views.recipes, name='recipes'),
    path('my-recipes/', views.my_recipes, name='my-recipes'),
    path('edit-recipe/<int:recipe_id>/', views.edit_recipe, name='edit-recipe'),
    path('like/', views.like_post, name='like_post'),
    path('filter/', views.filter_recipes, name='filter'), 
    path('delete-recipe/<int:recipe_id>/', views.delete_recipe, name='delete-recipe'),
    path('search/', views.search, name='search')
]
