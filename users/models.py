from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
#
# # Create your models here.
#
#
# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

class Student(models.Model):
    name = models.CharField(max_length=20)
    score = models.CharField(max_length=10)
