from django.shortcuts import render, redirect, reverse
from .forms import LecturerForm, UserRegistrationForm
from django.contrib import messages

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
    form = LecturerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('staffDashboard'))
    else:
        messages.error(request, "Something went wrong! Please try again")
        form = LecturerForm()
    return render(request, 'client/choices_form.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/reg.html', {'form': form})

