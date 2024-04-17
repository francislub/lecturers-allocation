from django import forms
from django.contrib.auth.hashers import make_password
# from .models import CustomUser, Department
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class DepartmentForm(forms.ModelForm):
#     class Meta:
#         model = Department
#         fields = ['name']

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'password', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['password'].widget.attrs['class'] = 'form-control'
		self.fields['password'].widget.attrs['placeholder'] = 'Password'
		self.fields['password'].label = ''
		self.fields['password'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


# class CustomUserForm(FormSettings):
#     email = forms.EmailField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput)
    
#     widget = {
#         'password': forms.PasswordInput(),
#     }

#     def __init__(self, *args, **kwargs):
#         super(CustomUserForm, self).__init__(*args, **kwargs)
#         if kwargs.get('instance'):
#             instance = kwargs.get('instance')
#             self.fields['password'].required = False
#             for field in CustomUser._meta.fields:
#                 if field.name not in ['id', 'user_ptr', 'password']:  # Exclude inherited fields
#                     self.fields[field.name].initial = getattr(instance, field.name)
#             if instance.pk is not None:
#                 self.fields['password'].widget.attrs['placeholder'] = "Fill this only if you wish to update password"
#         else:
#             self.fields['first_name'].required = True
#             self.fields['last_name'].required = True

#     def clean_email(self):
#         email = self.cleaned_data['email'].lower()
#         if self.instance.pk is None:  # Insert
#             if CustomUser.objects.filter(email=email).exists():
#                 raise forms.ValidationError("The given email is already registered")
#         else:  # Update
#             db_email = CustomUser.objects.get(id=self.instance.pk).email.lower()
#             if db_email != email:  # There has been changes
#                 if CustomUser.objects.filter(email=email).exists():
#                     raise forms.ValidationError("The given email is already registered")
#         return email

#     def clean_password(self):
#         password = self.cleaned_data.get("password", None)
#         if self.instance.pk is not None:
#             if not password:
#                 return self.instance.password
#         return make_password(password)

#     class Meta:
#         model = CustomUser
#         fields = ['last_name', 'first_name', 'email', 'password', 'department']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user
