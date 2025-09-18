from django.db import models
from django.contrib import admin
# Create your models here.

class Student_Detail(models.Model):
    Name=models.CharField(max_length=250, help_text="Enter your Name")
    Age=models.IntegerField(help_text="Enter your age")
    Dob=models.DateField(help_text="Enter your Date of Birth")
    Reg_no=models.IntegerField(help_text="Enter your Registration Number")

class Student_DetailAdmin(admin.ModelAdmin):
    list_display=('Name','Age','Dob','Reg_no')