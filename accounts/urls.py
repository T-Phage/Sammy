from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

# app_name = 'accounts'

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    # path('change_password/', views.changepasssword, name='change_password'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_complete.html'),
         name='password_reset_complete'),

    # change password
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'),
         name='password_change'),
    path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
]
