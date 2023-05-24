from django.contrib import admin

from .models import Teacher, Course, Lessons, File, MyCourse, Unit

# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'id', 'age', 'degree', 'status')
    list_filter = ('age','status')
    list_editable = ['status',]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'teacher', 'lesson_count', 'cost', 'status')
    list_filter = ('teacher','status', 'created_at')
    list_editable = ['status','cost']
    
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'course', 'status')
    list_filter = ('course','status', 'created_at')
    list_editable = ['status',]

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'unit','status', 'created_at')
    list_filter = ('unit','status', 'created_at')
    list_editable = ['status',]

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'status')
    list_filter = ('status',)
    list_editable = ['status',]


@admin.register(MyCourse)
class MyCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'id', 'status', 'created_at')
    list_filter = ('course', 'status', 'created_at')
    list_editable = ['status',]
