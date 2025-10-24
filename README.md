# Ex02 Django ORM Web Application
## Date: 18.9.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from.models import Student_Detail, Student_DetailAdmin

# Register your models here.

admin.site.register(Student_Detail,Student_DetailAdmin)
```
## OUTPUT
<img width="1920" height="1080" alt="ORM web app screenshot-1" src="https://github.com/user-attachments/assets/89c50e6f-5631-4519-9df7-65e27dd2eacc" />
<img width="1920" height="1080" alt="ORM web app screenshot-2" src="https://github.com/user-attachments/assets/7042bdf9-bf3c-4829-b3f5-1a347c3e4702" />

## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
