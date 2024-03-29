from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('lock/', views.lock, name='register'),
    path('dep/', views.dep, name='dep'),
    path('choices_form/', views.choices_form, name='choices_form'),
    path('',views.staffDashboard,name='staffDashboard'),
    path('client/', views.client, name='client'),
]