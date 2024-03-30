from django.shortcuts import render, reverse, redirect, get_object_or_404
# from client.models import Voter, Position, Candidate, Votes
#from account.models import Course
from administrator.models import Course,Lecturer
from account.forms import CustomUserForm

from administrator.forms import LecturerRegistration, CourseRegistration
# from client.forms import *
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.conf import settings

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('course_dashboard')

def dashboard(request):
    return render(request, "admin/dashboard.html")

def reqStatus(request):
    return render(request, "admin/reqStatus.html")

def reportStatus(request):
    return render(request, "admin/reportStatus.html")

def requistition_phase1(request):
    return render(request, "req.html")

def lecturerDa(request):
    lecturers = Lecturer.objects.all()
    return render(request, "admin/lecturer.html", {'lecturers':lecturers})

def courseDa(request):
    courses = Course.objects.all()
    return render(request, "admin/courseview.html", {'courses': courses})

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
    return render(request, 'admin/lectview.html', {'form': form})

def courseDashboard(request):
    if request.method == 'POST':
        form = CourseRegistration(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.id = form.cleaned_data['id']
            course.coursename = form.cleaned_data['coursename']
            course.semester = form.cleaned_data['semester']
            course.save()
            # form.save()
            return redirect(reverse('adminDashboard'))
    else:
        form = CourseRegistration()
    return render(request, 'admin/course.html', {'form': form})