import secrets
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from config import settings
from config.settings import EMAIL_HOST_USER
from users.forms import RegistrationForm
from users.models import User
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView


class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейди по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    '''Верификация пользователя'''
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserListView(ListView):
    model = User

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.exclude(email="admin@example.com")
        return queryset

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(pk=request.POST.get('status')).first()
        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True
        user.save()
        return redirect('user:user_list')


class UserUpdateView(UpdateView):
    model = User
    fields = ['email', 'phone', 'avatar', 'country']
    success_url = reverse_lazy('mailing:client_list')


class UserDetailView(DetailView):
    model = User



'''class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class UserListView(ListView):
    model = User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users:user_detail')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('mailing:mailing_start')'''
