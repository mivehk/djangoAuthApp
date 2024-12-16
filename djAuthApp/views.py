from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
#from .forms import CustomUserCreationForm

# Create your views here.
@login_required
def dashboard(request):
	return render(request, 'registration/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        #form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


