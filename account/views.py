from django.shortcuts import render, redirect, reverse
from .email_backend import EmailBackend
from django.contrib import messages
# from .forms import CustomUserForm, DepartmentForm, SignUpForm
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

# def account_login(request):
#     # if request.user.is_authenticated:
#     #     if user.user_type == '1':
#     #         return redirect(reverse("adminDashboard"))
#     #     elif user.user_type == '2':
#     #         return redirect(reverse("staffDashboard"))
#     #     else:
#     #         return redirect(reverse("cashierDashboard"))

#     # context = {}
#     if request.method == 'POST':
#         user = EmailBackend.authenticate(request, username=request.POST.get(
#             'email'), password=request.POST.get('password'))
#         if user != None:
#             login(request, user)
#             if user.user_type == '1':
#                 return redirect(reverse("adminDashboard"))
#             elif user.user_type == '2':
#                 return redirect(reverse("staffDashboard"))
#             else:
#                 return redirect(reverse("cashierDashboard"))
#         else:
#             messages.error(request, "Invalid details")
#             return redirect("adminDashboard")

#     return render(request, "auth/login.html")


# def account_register(request):
#     userForm = CustomUserForm(request.POST or None)
#     context = {
#         'form1': userForm,
#     }
#     if request.method == 'POST':
#         if userForm.is_valid():
#             user = userForm.save(commit=False)
#             user.department = userForm.cleaned_data['department']
#             user.save()
#             messages.success(request, "Account created. You can login now!")
#             return redirect(reverse('account_login'))
#         else:
#             messages.error(request, "Provided data failed validation")
#             # return account_login(request)
#     return render(request, "auth/reg.html", context)

# def login(request):
# 	# Check to see if logging in
# 	if request.method == 'POST':
# 		email = request.POST['email']
# 		password = request.POST['password']
# 		# Authenticate
# 		# user = authenticate(request, email=email, password=password)
# 		# print(user)
# 		# user = User.objects.filter(email=email).filter(password=password)
# 		if email == 'karemera@gmail.com' and password == 'karemera':
# 		# if user is not None:
# 			# login(request, user)
# 			messages.success(request, "You Have Been Logged In!")
# 			return redirect('adminDashboard')
# 		elif email == 'karemera@gmail.com' and password == 'charles':
# 			messages.success(request, "You Have Been Logged In!")
# 			return redirect('staffDashboard')
# 		else:
# 			messages.success(request, "There Was An Error Logging In, Please Try Again...")
# 			return redirect('login')
# 	else:
# 		return render(request, 'auth/login.html')
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        category = request.POST.get('category')

        if email and password and category:  # Check if all required fields are present
            user = authenticate(request, email=email, password=password)
            if user is not None and user.category == category:
                login(request, user)
                if category == 'Administrator':
                    return redirect('adminDashboard')
                elif category == 'Lecturer':
                    return redirect('staffDashboard')
            else:
                messages.error(request, "Invalid credentials or category.")
        else:
            messages.error(request, "Please provide email, password, and category.")

    return render(request, 'auth/login.html')

def register_user(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        category = request.POST['category']
        try:
            user = User.objects.create_user(email=email, password=password, first_name=firstname, last_name=lastname, category=category)
            messages.success(request, "Registration successful. You can now login.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Registration failed: {e}")
    return render(request, 'auth/reg.html')

# def register_user(request):
# 	if request.method == 'POST':
# 		print(request)
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			# Authenticate and login
# 			# email = form.cleaned_data['email']
# 			# password = form.cleaned_data['password']
# 			# user = authenticate(email=email, password=password)
# 			# print(user)
# 			# if user is not None:
# 			# 	login(user)
# 		messages.success(request, "You Have Successfully Registered! Welcome!")
# 		return redirect('login')
# 	else:
# 		form = SignUpForm()
# 		return render(request, 'auth/reg.html', {'form':form})

# 	return render(request, 'auth/reg.html', {'form':form})


def account_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        messages.success(request, "Thank you for visiting us!")
    else:
        messages.error(
            request, "You need to be logged in to perform this action")

    return redirect(reverse("account_login"))

def lock(request):
    return render(request, 'auth/lock_screen.html')

# def create_department(request):
#     form = DepartmentForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('account_login')  
#     else:
#         messages.error(request, "Provided data failed validation")
#     return render(request, 'dep.html', {'form': form})