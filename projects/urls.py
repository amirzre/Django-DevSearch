from django.urls import path
from . import views


app_name = 'projects'

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.project, name='project'),
    path('projects/create/', views.createProject, name='create_project'),
    path('projects/update/<int:pk>/',
         views.updateProject, name='update_project'),
    path('projects/delete/<int:pk>/',
         views.deleteProject, name='delete_project'),
]
