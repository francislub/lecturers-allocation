from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('lock/', views.lock, name='register'),
    path('dep/', views.dep, name='dep'),
    path('req/', views.requisition_phase1, name='requisition_phase1'),
    path('',views.staffDashboard,name='staffDashboard'),
    path('client/', views.client, name='client'),
]