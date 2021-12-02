from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user_profile'),
]
