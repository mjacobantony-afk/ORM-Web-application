from django.contrib import admin
from.models import Student_Detail, Student_DetailAdmin

# Register your models here.

admin.site.register(Student_Detail,Student_DetailAdmin)