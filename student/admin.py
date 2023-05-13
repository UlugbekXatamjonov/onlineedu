from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'id', 'age', 'email', 'gender', 'status']
    list_filter = ('age', 'gender', 'status', 'created_at')
    list_editable = ['status']

