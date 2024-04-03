from django.urls import path
from . import views
from .views import delete_course,delete_lecturer,update_course

urlpatterns = [
    path('', views.dashboard, name="adminDashboard"),
    path('reqst/', views.reqStatus, name="reqst"),
    path('repst/', views.reportStatus, name="repst"),
    path('requistition_phase1/', views.requistition_phase1, name="requistition_phase1"),
    path('lecturer/', views.lecturerDa, name="lecturer"),
    path('lectview/', views.lecturerDashboard, name="lectview"),
    path('courseview/', views.courseDa, name="courseview"),
    path('course/', views.courseDashboard, name="course"),
    path('choices/', views.choicesDashboard, name="choices"),
    path('courses/delete/<int:course_id>/', delete_course, name='delete_course'),
    path('courses/update/<int:course_id>/', update_course, name='update_course'),
    path('lecturers/delete/<int:lecturer_id>/', delete_lecturer, name='delete_lecturer'),
    #path('get-courses/', get_courses_by_semester, name='get_courses_by_semester'),
    #path('get-courses/', views.get_courses, name='get_courses'),
  
]