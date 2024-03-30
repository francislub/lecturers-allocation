from django.shortcuts import render, redirect, reverse
from .forms import LecturerForm

# Create your views here.

def login(request):
    return render(request, 'auth/login.html')

def register(request):
    return render(request, 'auth/reg.html')

def lock(request):
    return render(request, 'auth/lock_screen.html')

def dep(request):
    return render(request, 'dep.html')

def req(request):
    return render(request, 'client/req.html')


#===========Francis calling the dashbourd==============
def staffDashboard(request):
    return render(request, 'client/staffDash.html')

def client(request):
    return render(request, 'client.html')


def choices_form(request):
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(reverse('staffDashboard'))
    else:
        form = LecturerForm()
    return render(request, 'client/choices_form.html', {'form': form})

