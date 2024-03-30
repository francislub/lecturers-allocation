from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, Submit
from .models import Lecturer

class LecturerForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column(css_class='col-md-3'),
    #             Field('semester', css_class='form-control selectpicker'),  # Use custom class
    #             Column(css_class='col-md-3'),
    #             Field('id', css_class='form-control'),
    #         ),
    #         Row(
    #             Column(css_class='col-md-3'),
    #             Field('name', css_class='form-control'),
    #             Column(css_class='col-md-3'),
    #             Field('qualification', css_class='form-control'),
    #         ),
    #         Row(
    #             Column(css_class='col-md-3'),
    #             Field('experience', css_control='form-control'),
    #             Column(css_class='col-md-3'),
    #             Field('publication', css_class='form-control'),
    #         ),
    #         Submit('submit', 'Submit', css_class='btn btn-secondary'),
    #     )
    # id = forms.CharField()
    # name = forms.CharField()
    # qualification = forms.CharField()
    # experience = forms.CharField()
    # publication = forms.CharField()
    # semester = forms.CharField()

    class Meta:
        model = Lecturer
        exclude = ("user",)
