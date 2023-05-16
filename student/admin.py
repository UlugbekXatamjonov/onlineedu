from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'id', 'status']
    list_filter = ('status', 'created_at')
    list_editable = ['status',]

