from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
#from administrator.models import CustomUser, Department
class Course(models.Model):
    # Existing fields
    
    id = models.CharField(primary_key=True, max_length=100)
    coursename = models.CharField(max_length=300, null=True, blank=True)
    semester = models.CharField(max_length=255, null=True, blank=True)
    
class Lecturer(models.Model):
    # Existing fields
    id = models.CharField(primary_key=True, max_length=100)
    lecturername = models.CharField(max_length=200, null=True, blank=True)
    qualification = models.CharField(max_length=255, null=True, blank=True)
    semester = models.CharField(max_length=255, null=True, blank=True)
    coursename = models.CharField(max_length=255, null=True, blank=True)
    feedback = models.CharField(max_length=255, null=True, blank=True)
    experience = models.CharField(max_length=255, null=True, blank=True)
    professional = models.CharField(max_length=255, null=True, blank=True)
    publication = models.CharField(max_length=255, null=True, blank=True)
    
    
    
    # received_by = models.CharField(max_length=100, null=True, blank=True)
    # date_received = models.DateTimeField(null=True, blank=True)
    # cashier_signature = models.ImageField(upload_to='cashier_signatures/', null=True, blank=True)
    # receiver_signature = models.ImageField(upload_to='receiver_signatures/', null=True, blank=True)
    # voucher_number = models.CharField(max_length=100, null=True, blank=True)