from django.db import models
from account.models import CustomUser, Department
    
class Lecturer(models.Model):
    # Existing fields
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, null=True, blank=True)
    semester = models.CharField(max_length=100, null=True, blank=True)
    qualification = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=100, null=True, blank=True)
    publication = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"Lecturer #{self.pk}"

