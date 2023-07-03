from django.shortcuts import render
from django.contrib.auth import views as auth_views

# Create your views here.

class LoginView(auth_views.LoginView):
     template_name = 'staff/login.html'
    
class LogoutView(auth_views.LogoutView):
     template_name = 'staff/logout.html'

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
     template_name = 'staff/password_change_done.html'

class PasswordChangeView(auth_views.PasswordChangeView):
     template_name = 'staff/password_change.html'

class PasswordResetCompleteView (auth_views.PasswordResetCompleteView):
     template_name = 'staff/password_reset_complete.html'

class PasswordResetConfirmView (auth_views.PasswordResetConfirmView):
     template_name = 'staff/password_reset_confirm.html'

class PasswordResetDoneView (auth_views.PasswordResetDoneView):
     template_name = 'staff/password_reset_done.html'    

class PasswordResetView (auth_views.PasswordResetView):
     template_name = 'staff/password_reset.html'  