# user_registration/urls.py

from django.urls import path
from .views import signup, user_login, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup, name='user-registration'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
