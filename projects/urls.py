from django.urls import path
from . import views


app_name = 'projects'

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('projects/<str:pk>/', views.project, name='project'),
    path('project/create/', views.createProject, name='create_project'),
    path('project/update/<int:pk>/',
         views.updateProject, name='update_project'),
    path('project/delete/<int:pk>/',
         views.deleteProject, name='delete_project'),
]
