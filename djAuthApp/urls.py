from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # User registration
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login view
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),  # Logout view
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard for logged-in users
]

