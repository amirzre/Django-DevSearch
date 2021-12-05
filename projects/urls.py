from django.urls import path
from . import views


app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('create/', views.createProject, name='create_project'),
    path('update/<str:pk>/',
         views.updateProject, name='update_project'),
    path('delete/<str:pk>/',
         views.deleteProject, name='delete_project'),
]
