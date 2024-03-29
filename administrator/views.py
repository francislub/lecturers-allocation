from django.shortcuts import render, reverse, redirect
# from client.models import Voter, Position, Candidate, Votes
from account.models import CustomUser
from account.forms import CustomUserForm
# from client.forms import *
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.conf import settings

def dashboard(request):
    return render(request, "admin/dashboard.html")

def reqStatus(request):
    return render(request, "admin/reqStatus.html")

def reportStatus(request):
    return render(request, "admin/reportStatus.html")

def requisition_phase1(request):
    return render(request, "admin/req.html")

def requistition_phase1(request):
    return render(request, "admin/req.html")

def lecturerDashboard(request):
    if request.method == 'POST':
        form = LecturerRegistration(request.POST)
        if form.is_valid():
            lecturer = form.save(commit=False)
            lecturer.id = form.cleaned_data['id']
            lecturer.lecturername = form.cleaned_data['lecturername']
            lecturer.qualification = form.cleaned_data['qualification']
            lecturer.publication = form.cleaned_data['publication']
            lecturer.semester = form.cleaned_data['semester']
            lecturer.save()
            return redirect(reverse('adminDashboard'))
    else:
        form = LecturerRegistration()
    return render(request, 'admin/lecturer.html', {'form': form})