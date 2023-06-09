from django.contrib import admin
from .models import Student, Contact

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'id', 'status']
    list_filter = ('status', 'created_at')
    list_editable = ['status',]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ['status',]



