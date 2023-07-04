from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, authenticate, login
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm, UserForm, ProfileForm
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.utils.text import gettext_lazy as _





# Create your views here.

class LoginView(auth_views.LoginView):
     template_name = 'staff/login.html'
    
class LogoutView(auth_views.LogoutView):
     template_name = 'staff/logout.html'

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
     template_name = 'staff/password_change_done.html'

class PasswordChangeView(auth_views.PasswordChangeView):
     template_name = 'staff/password_change.html'
     success_url = reverse_lazy('staff:password_change_done')

class PasswordResetCompleteView (auth_views.PasswordResetCompleteView):
     template_name = 'staff/password_reset_complete.html'

class PasswordResetConfirmView (auth_views.PasswordResetConfirmView):
     template_name = 'staff/password_reset_confirm.html'
     success_url = reverse_lazy('staff:password_reset_complete')

class PasswordResetDoneView (auth_views.PasswordResetDoneView):
     template_name = 'staff/password_reset_done.html'    

class PasswordResetView (auth_views.PasswordResetView):
     template_name = 'staff/password_reset.html'  
     success_url = reverse_lazy('staff:password_reset_done')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'staff/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'staff/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'staff/register.html', {'user_form': user_form})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Ваш профиль был успешно обновлен!'))
            return redirect('staff:edit')
        else:
            messages.error(request, _('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'staff/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })