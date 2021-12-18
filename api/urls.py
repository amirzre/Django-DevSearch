from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from . import views


app_name = 'api'

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', views.getRoutes, name='routes'),
    path('projects/', views.getProjects, name='projects'),
    path('projects/<int:pk>/', views.getProject, name='project'),
    path('projects/<int:pk>/vote/', views.projectVote, name='project_vote'),
    path('removetag/', views.removeTag, name='remove_tag'),
]
