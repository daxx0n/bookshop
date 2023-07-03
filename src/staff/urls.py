from django.urls import path
from . import views
app_name = 'staff'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name = "login"),
    path('logout/', views.LogoutView.as_view(), name = "logout"),
    path('password_change/', views.PasswordChangeView.as_view(), name= "password_change"),
    path('accounts/password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]