from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="adminDashboard"),
    path('reqst/', views.reqStatus, name="reqst"),
    path('repst/', views.reportStatus, name="repst"),
    path('requisition_phase1/', views.requisition_phase1, name='requisition_phase1'),
]