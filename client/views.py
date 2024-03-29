from django.shortcuts import render, redirect, reverse
from .forms import RequisitionPhase1Form, RequisitionPhase2Form, RequisitionPhase3Form

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
        form = RequisitionPhase1Form(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.department = form.cleaned_data['department']
            requisition.requester = form.cleaned_data['requester']
            requisition.phase = 1
            requisition.save()
            return redirect(reverse('staffDashboard'))
    else:
        form = RequisitionPhase1Form()
    return render(request, 'client/choices_form.html', {'form': form})

def requisition_phase2(request):
    if request.method == 'POST':
        form = RequisitionPhase2Form(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.phase = 2
            requisition.save()
            return redirect('requisition_phase2')
    else:
        form = RequisitionPhase2Form()
    return render(request, 'requisition_phase2.html', {'form': form})

def requisition_phase3(request):
    if request.method == 'POST':
        form = RequisitionPhase3Form(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.phase = 3
            requisition.save()
            return redirect('requisition_phase3')
    else:
        form = RequisitionPhase3Form()
    return render(request, 'requisition_phase3.html', {'form': form})
