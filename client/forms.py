from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, Submit
from .models import Lecturer

class LecturerForm(forms.ModelForm):

    class Meta:
        model = Lecturer
        fields = ['semester', 'name', 'qualification', 'experience', 'id', 'publication']
