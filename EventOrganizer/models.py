from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
import datetime, os

class on(models.Model):
    name=models.TextField(max_length=30)
    img=models.ImageField(upload_to="media")
    desc=models.TextField(max_length=500)
    class Meta:
        db_table='EventOrganizer_ongoing'

class rev(models.Model):
    user=models.TextField(max_length=101)
    description=models.TextField(max_length=900, null=True)
    rating=models.TextField(max_length=10)
    class Meta:
        db_table='EventOrganizer_re'

class contact(models.Model):
    name=models.TextField(max_length=30)
    email=models.TextField(max_length=80)
    number=models.TextField(max_length=20)
    subject=models.TextField(max_length=50)
    message=models.TextField(max_length=300)
    class Meta:
        db_table='EventOrganizer_contact'

# class signupDB(UserCreationForm):
#     uname=models.TextField(max_length=30)
#     email=models.TextField(max_length=80)
#     password=models.TextField(max_length=20)
#     pRepeat=models.TextField(max_length=50)
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2', )
