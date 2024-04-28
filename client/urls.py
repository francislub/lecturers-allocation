from django.urls import path
from . import views
# from .views import courseDashboard, delete_course

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    path('register/', views.register, name='acc_register'),
    # path('lock/', views.lock, name='lock'),
    path('dep/', views.dep, name='dep'),
    path('choices_form/', views.choices_form, name='choices_form'),
    path('',views.staffDashboard,name='staffDashboard'),
    path('client/', views.client, name='client'),
    # path('course-dashboard/', courseDashboard, name='course_dashboard'),
    # path('delete-course/<int:course_id>/', delete_course, name='delete_course'),
]