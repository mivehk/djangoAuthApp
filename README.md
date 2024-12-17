# Django Authentication Project

This project demonstrates a Django-based authentication system engaging user registration, login, logout, and a restricted dashboard for authenticated users. It also uses custom view templates for better user experience.

---

## **Features**
- User registration and authentication
- Login and logout functionality
- Restricted dashboard access using `login_required`
- Custom templates for authentication views (Bootstrap-ready)
- SQLite database for local development

---

## **Getting Started**

### **1. Install Django and Create the Project**
Install Django and set up the project directory:
```bash
python3 -m pip install django
django-admin startproject "your-project-name"
cd myproject
python manage.py startapp "your-app-name, e.g., djAuthApp"
```

### **2. Enable the App and verify BASE_DIR variable (e.g., pathlib )**
```bash
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth',  # Authentication system 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles',
    'djAuthApp',  # Your custom app for authentication 
]
```

### **3. Include URLs for Project Authentication**
```bash
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djAuthApp/', include('djAuthApp.urls')),  # Include child URLs within your djAuthApp's application
]
```

### **4. Create Custom Login and Logout Templates (e.g., using bootstrap templates)**
``` bash
│   ├── templates
│   │   ├── base.html
│   │   └── registration
│   │       ├── dashboard.html
│   │       ├── login.html
│   │       ├── logout.html
│   │       └── register.html

update TEMPLATES section of django settings for the directory path of templates
'DIRS': [BASE_DIR / 'templates'],
```

### **5. Add Django’s Authentication Views for the application URLs**
```bash
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),  
    path('dashboard/', views.dashboard, name='dashboard'), 
]
```

### **6- Create Restricted login_required dashboard view and another one for register**

```bash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def dashboard(request):
	return render(request, 'registration/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

```

###**7- Include new routes into settings**
```bash
LOGIN_REDIRECT_URL = '/djAuthApp/dashboard/'
LOGOUT_REDIRECT_URL = '/djAuthApp/login'
LOGIN_URL = '/djAuthApp/login'
```

###**8- Generate migration files and apply them on db**
```bash
python manage.py makemigrations
python manage.py migrate
```

###**9- Run django server**
```bash
python manage.py runserver
```

###**10- create superuser (optional)**
```bash
python3 manage.py createsuperuser
Username: admin
Email address: xxxxxx@xxx.com
Password: 
Password (again): 
Superuser created successfully.
```




