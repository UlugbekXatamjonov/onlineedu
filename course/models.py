from django.db import models
from autoslug import AutoSlugField

from student.models import Student
# Create your models here.


class Teacher(models.Model):
    full_name = models.CharField(max_length=111)
    age = models.PositiveIntegerField()
    slug = AutoSlugField(populate_from = 'full_name',unique=True)
    degree = models.CharField(max_length=51)# teacher darajasi
    about = models.TextField()
    
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "O'qtuvchi"
        verbose_name_plural = "O'qtuvchilar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.full_name

class Course(models.Model):
    name = models.CharField(max_length=111,unique=True)
    slug = AutoSlugField(populate_from = 'name', unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    lesson_count = models.PositiveIntegerField()
    cost = models.PositiveIntegerField(verbose_name='pul uchun',null=True)
    photo = models.ImageField(upload_to='course_photo/%Y/%m/%d/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

class Lessons(models.Model):
    name = models.CharField(max_length=61)
    slug = AutoSlugField(populate_from = 'name',unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='lessons')
    about = models.TextField(verbose_name="dars haqida")
    video = models.URLField(blank=True, null=True)
    body = models.TextField(verbose_name="Dars matni", blank=True, null=True)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"
        ordering = ('created_at',)

    def __str__(self):
        return self.name

def slug_funckion_for_file_model(self):
        """ Ikkita maydonni sludada birlashtirish """
        return "{}-file-".format(self.lesson.name)

class File(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='cours_file')
    slug = AutoSlugField((u'slug'), populate_from=slug_funckion_for_file_model, unique=True)

    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Fayl'
        verbose_name_plural = 'Fayllar'

    def __str__(self) -> str:
        return self.lesson.name

def slug_funckion_for_mycourse_model(self):
        """ Ikkita maydonni sludada birlashtirish """
        return "{}-{}".format(self.student.first_name, self.course.name)

class MyCourse(models.Model):   
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='my_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,)
    slug = AutoSlugField((u'slug'), populate_from = slug_funckion_for_mycourse_model, unique=True)
    ball = models.PositiveIntegerField(default=0)
    coin = models.PositiveIntegerField(default=0)
    next_lesson = models.PositiveIntegerField( blank=True, null=True)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mening kursim"
        verbose_name_plural = "Mening kurslarim"

    def __str__(self):
        return f"{self.course.name}"

    