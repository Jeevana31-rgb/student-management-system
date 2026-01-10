from django.contrib import admin
from .models import User, Student, Course

# Simple basic admin registration without custom classes
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Student)

# Customize admin site headers
admin.site.site_header = "Student Management Admin"
admin.site.site_title = "Student Management"
admin.site.index_title = "Welcome to Student Management Administration"
