from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from users.views import (UserCreateView, UserListView,
                         email_verification, UserDetailView, UserUpdateView)

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    #path('login/', LoginView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    #path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    #path('change/<int:pk>/', UserUpdateView.as_view(), name='user_update'),


]