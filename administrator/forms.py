from django import forms
from .models import Lecturer, Course

class LecturerRegistration(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['id', 'lecturername', 'qualification','semester','courseunits','feedback','experience','professional','publication']  # Include request date field

class CourseRegistration(forms.ModelForm):
    #request_date = forms.DateTimeField(label='Request Date', required=False)  # Add request date field
    
    class Meta:
        model = Course
        fields = ['id', 'coursename', 'semester']  # Include request date field
        
class SemesterForm(forms.Form):
    semester = forms.ChoiceField(choices=[('', 'Select Semester'), ('First Semester', 'First Semester'), ('Second Semester', 'Second Semester')])

#class RequisitionPhase2Form(forms.ModelForm):
#    supervisor_date = forms.DateTimeField(label='Supervisor Approval Date', required=False)  # Add supervisor date field
    
#    class Meta:
#        model = Requisition
#        fields = ['supervisor', 'supervisor_comment', 'supervisor_date']  # Include supervisor date field

#class RequisitionPhase3Form(forms.ModelForm):
#    approver_date = forms.DateTimeField(label='Approver Approval Date', required=False)  # Add approver date field
    
#    class Meta:
#        model = Requisition
#        fields = ['approver', 'charge_to_account', 'approver_date']  # Include approver date field
