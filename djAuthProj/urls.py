"""
URL configuration for djAuthProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
from django.contrib import admin
from django.urls import path , include #imported include to add djAuthApp url

from django.contrib.auth import views as auth_views

## i used a separate script to add project directory to sys.path
##PosixPath('/Users/kmive/Desktop/python/django_Auth_Project/djAuthProj')
from djAuthApp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djAuthApp/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
]"""

from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djAuthApp/', include('djAuthApp.urls')),  # Include djAuthApp's URLs
]


