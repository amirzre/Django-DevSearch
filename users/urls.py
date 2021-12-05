from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user_profile'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', views.userAccount, name='account'),
]
