from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="adminDashboard"),
    path('reqst/', views.reqStatus, name="reqst"),
    path('repst/', views.reportStatus, name="repst"),
    path('requistition_phase1/', views.requistition_phase1, name="requistition_phase1"),
    path('lecturer/', views.lecturerDashboard, name="lecturer"),
    
]