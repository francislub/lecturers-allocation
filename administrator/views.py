from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Course
from django.db import IntegrityError
# from client.models import Voter, Position, Candidate, Votes
#from account.models import Course
from administrator.models import Course,Lecturer
# from account.forms import CustomUserForm
from .forms import SemesterForm


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

def delete_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, pk=lecturer_id)
    if request.method == 'POST':
        lecturer.delete()
        return redirect('lecturer')  # Redirect to the desired page after deletion
    # Optionally, render a confirmation page for deletion
    return render(request, 'admin/confirm_delete_lecturer.html', {'lecturer': lecturer})

def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courseview')  # Redirect to the desired page after deletion
    # Optionally, you can render a confirmation page for deletion
    return render(request, 'admin/confirm_delete.html', {'course': course})

def lecturerDashboard(request):
    if request.method == 'POST':
        form = LecturerRegistration(request.POST)
        if form.is_valid():
            semester = form.cleaned_data['semester']
            for course in form.cleaned_data['coursename']:  # Assuming 'coursename' represents multiple course selections
                id = form.cleaned_data['id']
                # Check if the id is unique before creating the lecturer
                if not Lecturer.objects.filter(id=id).exists():
                    lecturer = Lecturer.objects.create(
                        id=id,
                        lecturername=form.cleaned_data['lecturername'],
                        qualification=form.cleaned_data['qualification'],
                        coursename=form.cleaned_data['coursename'],
                        feedback=form.cleaned_data['feedback'],
                        experience=form.cleaned_data['experience'],
                        professional=form.cleaned_data['professional'],
                        publication=form.cleaned_data['publication'],
                        semester=semester
                    )
                else:
                    form = LecturerRegistration()
                return redirect('lecturer')
            return HttpResponse('Lecturer(s) created successfully')
        else:
            return HttpResponse('Please enter a different lecturer id!')
    else:
        form = LecturerRegistration()
    # return render(request, 'admin/lecturer.html', {'form': form})
    return redirect('lecturer')
# def lecturerDashboard(request):
#     if request.method == 'POST':
#         form = LecturerRegistration(request.POST)
#         if form.is_valid():
#             semester = form.cleaned_data['semester']
#             courses = form.cleaned_data['courses']
#             lecturer_id = form.cleaned_data['id']
#             lecturer_name = form.cleaned_data['lecturername']
#             qualification = form.cleaned_data['qualification']
#             for course in courses:
#                 feedback = form.cleaned_data['feedback']
#                 experience = form.cleaned_data['experience']
#                 professional = form.cleaned_data['professional']
#                 publication = form.cleaned_data['publication']
                
#                 lecturer = Lecturer.objects.create(
#                     id=lecturer_id,
#                     lecturername=lecturer_name,
#                     qualification=qualification,
#                     semester=semester,
#                     course=course,
#                     feedback=feedback,
#                     experience=experience,
#                     professional=professional,
#                     publication=publication
#                 )
#                 # You can perform additional operations or validation here if needed

#             return redirect('lecturer')
#     else:
#         form = LecturerRegistration()
#     return redirect('lecturer')

# def courseDashboard(request):
#     courses = Course.objects.all()  # Query all courses from the database
#     return render(request, 'admin/course.html', {'courses': courses})

def get_courses(request):
    semester = request.GET.get('semester')
    courses = Course.objects.filter(semester=semester)
    data = [{'id': course.id, 'coursename': course.name} for course in courses]
    return JsonResponse(data, safe=False)

def courseDashboard(request):
    if request.method == 'POST':
        form = CourseRegistration(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.id = form.cleaned_data['id']
            course.coursename = form.cleaned_data['coursename']
            course.semester = form.cleaned_data['semester']
            course.save()
            form.save()
            return redirect(reverse('courseview'))
    else:
        form = CourseRegistration()
    return render(request, 'admin/course.html', {'form': form})

def update_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = CourseRegistration(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courseview')  # Assuming 'courseview' is the URL name for displaying course details
    else:
        form = CourseRegistration(instance=course)
    return render(request, 'admin/courseupdate.html', {'form': form})

def update_lecturer(request, lecturer_id):
    lecturer = Lecturer.objects.get(pk=lecturer_id)
    if request.method == 'POST':
        form = LecturerRegistration(request.POST, instance=lecturer)
        if form.is_valid():
            form.save()
            return redirect('lecturer')  # Assuming 'courseview' is the URL name for displaying course details
    else:
        form = LecturerRegistration(instance=lecturer)
    return render(request, 'admin/lecturerupdate.html', {'form': form})

def view_lecturer(request, lecturer_id):
    lecturer = Lecturer.objects.get(pk=lecturer_id)
    if request.method == 'POST':
        form = LecturerRegistration(request.POST, instance=lecturer)
        if form.is_valid():
            form.view()
            return redirect('lecturer')  # Assuming 'courseview' is the URL name for displaying course details
    else:
        form = LecturerRegistration(instance=lecturer)
    return render(request, 'admin/lecturerview.html', {'form': form})

def choicesDashboard(request):
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
    return render(request, 'admin/choices.html', {'form': form})
def approval_form(request):
    # form = SemesterForm(request.POST)
    semester = request.POST.get('semester')
    courses = Course.objects.filter(semester=semester)
    if request.method == 'POST':
        if semester:
            return render(request, 'admin/lectview.html', {'courses': courses, 'semester':semester})
        else:
            return render(request, 'lecturer.html', {'error': 'Please select a semester.'})
        
        # if form.is_valid():
        #     semester = form.cleaned_data['semester']
        #     if semester:
        #         return redirect('lectview')  # Redirect to lectview if semester is selected
        #     else:
        #         return render(request, 'admin/lecturersemester.html', {'form': form, 'error': 'Please select a semester.'})
    else:
        form = SemesterForm()
    return render(request, 'admin/lecturersemester.html', {'form': form})

def lectview(request):
    return render(request, 'lecturer.html')  # Render the form initially
