from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls', namespace='projects')),
    path('', include('users.urls', namespace='users')),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='reset_password.html'),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='reset_password_sent.html'),
         name='passowrd_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='reset.html'),
         name='passowrd_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='passowrd_reset_complete.html'),
         name='passowrd_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
