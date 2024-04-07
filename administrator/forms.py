from django import forms
from .models import Lecturer, Course

class LecturerRegistration(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['id', 'lecturername', 'qualification','coursename','feedback','experience','professional','publication','semester']  # Include request date field

class CourseRegistration(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ['id', 'coursename', 'semester']  # Include request date field
        
class SemesterForm(forms.Form):
    semester = forms.ChoiceField(choices=[('', 'Select Semester'), ('First Semester', 'First Semester'), ('Second Semester', 'Second Semester')])