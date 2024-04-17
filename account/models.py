# from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone

# class Department(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class CustomUserManager(UserManager):
#     def _create_user(self, email, password, **extra_fields):
#         email = self.normalize_email(email)
#         user = CustomUser(email=email, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("user_type", 1)
#         extra_fields.setdefault("last_name", "System")
#         extra_fields.setdefault("first_name", "Administrator")

#         assert extra_fields["is_staff"]
#         assert extra_fields["is_superuser"]
#         return self._create_user(email, password, **extra_fields)


# class CustomUser(AbstractUser):
#     USER_TYPE = ((1, "Admin"), (2, "staff"), (3, "cashier"))
#     username = None 
#     user_type = models.CharField(default=2, choices=USER_TYPE, max_length=1)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
#     email = models.EmailField(unique=True)
#     full_name = models.CharField(max_length=255, blank=True)
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#     objects = CustomUserManager()
#     department = models.ForeignKey(Department, related_name='users', on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.last_name + " " + self.first_name

