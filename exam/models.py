from django.db import models

from autoslug import AutoSlugField

from course.models import Lessons
from student.models import Student

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        # ordering = ('-created_at',)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kichik kategoriya"
        verbose_name_plural = "Kichik kategoriyalar"
        # ordering = ('-created_at',)

    def __str__(self):
        return self.name

class Examp(models.Model):
    """ Imtihon modeli """
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE,related_name='lsn')
    name = models.CharField(max_length=111)
    slug = AutoSlugField(populate_from = 'name',unique=True)
    main_examp = models.BooleanField(default=False, null=True, blank=True)
    about = models.TextField()
    time = models.PositiveIntegerField(verbose_name='Vaqt',null=True)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Imtihon"
        verbose_name_plural = "Imtihonlar"
        # ordering = ['-created_at',]

    def __str__(self) -> str:
        return self.name

class Question(models.Model):
    """ Imtihon va darsdan keyin beriladigan imtihon uchun savollar """
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    examp = models.ForeignKey(Examp, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)

    question_text = models.CharField(max_length=123)
    
    status = models.BooleanField(default=True,)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"
        # ordering = ['created_at',]

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    """ Savol javoblari uchun models """
    question = models.ForeignKey(Question, related_name='answers',on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=221,verbose_name='Answer Text')
    # true_answer - To'g'ri javob maydoni
    true_answer = models.BooleanField(default=False)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Javob"
        verbose_name_plural = "Javoblar"
        # ordering = ['-created_at',]

    def __str__(self):
        return self.answer_text

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="results", blank=True, null=True)
    examp = models.ForeignKey(Examp, on_delete=models.CASCADE, related_name="results", blank=True, null=True)
    ball = models.PositiveIntegerField(default=0, blank=True, null=True)
    coin = models.PositiveIntegerField(default=0, blank=True, null=True)
    # answers - o'quvchining belgilagan javovblari yuboriladigan maydon
    answers = models.JSONField(null=True, blank=True)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.student.first_name

class FreeResult(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="free_results", blank=True, null=True)
    ball = models.PositiveIntegerField(default=0, blank=True, null=True)
    # answers - o'quvchining belgilagan javovblari yuboriladigan maydon
    answers = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Free Natija"
        verbose_name_plural = "Free Natijalar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.subcategory.name


