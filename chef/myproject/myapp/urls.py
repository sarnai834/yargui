from django.urls import path
from myapp import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('home/add_food/', views.add_food, name='add_food'),
    path('home/food_list/', views.food_list, name='food_list'),
    path('home/add_menu/', views.add_menu, name='add_menu'), 
    path('home/menu_list/', views.menu_list, name='menu_list'),
    path('home/menu_search/', views.menu_search, name='menu_search'),
    path('home/calculate_calories/', views.calculate_calories, name='calculate_calories'),
]
