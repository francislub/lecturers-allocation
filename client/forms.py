from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, Submit
from .models import Lecturer,ClientUser

class LecturerForm(forms.ModelForm):

    class Meta:
        model = Lecturer
        fields = ['semester', 'name', 'qualification', 'experience', 'id', 'publication']
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = ClientUser
        fields = ['firstname', 'lastname', 'category', 'email', 'password', 'terms_accepted']
