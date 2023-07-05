from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, authenticate, login
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.utils.text import gettext_lazy as _
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm, ProfileForm
from proj.services.utils import unique_slugify
from django.views.generic import DetailView, UpdateView, CreateView
from .forms import UserUpdateForm, ProfileUpdateForm, UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView




from .forms import UserRegisterForm
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
            return redirect('staff:profile')
        else:
            messages.error(request, _('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'staff/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

class ProfileDetailView(DetailView):
    """
    Представление для просмотра профиля
    """
    model = Profile
    context_object_name = 'profile'
    template_name = 'staff/profile_detail.html'
    queryset = model.objects.all().select_related('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Страница пользователя: {self.object.user.username}'
        return context


class ProfileUpdateView(UpdateView):
    """
    Представление для редактирования профиля 
    """
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'staff/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля пользователя: {self.request.user.username}'
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('staff:profile_detail', kwargs={'slug': self.object.slug})

class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = 'staff/user_register.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context

class UserLoginView(SuccessMessageMixin, LoginView):
    """
    Авторизация на сайте
    """
    form_class = UserLoginForm
    template_name = 'staff/user_login.html'
    next_page = 'Home Page'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context

    
class UserLogoutView(LogoutView):
    """
    Выход с сайта
    """
    next_page = 'Home Page'