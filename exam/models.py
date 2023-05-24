from django.db import models

from autoslug import AutoSlugField

from course.models import Lessons
from student.models import Student

# Create your models here.

EXAMP_TYPE = (
    ('always',"Doimiy imtihonlar"),
    ('dayly',"Kunlik imtihonlar"),
    ('weekly', "Haftalik imtihonlar"),
    ('monthly', "Oylik imtihonlar"),
)

""" Free bo'limi - ro'yhatdan o'tmagan userlar uchun ochiq testlar to'plami """
class FreeCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ochiq Kategoriya"
        verbose_name_plural = "Ochiq Kategoriyalar"
        # ordering = ('-created_at',)

    def __str__(self):
        return self.name

class FreeSubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)
    category = models.ForeignKey(FreeCategory, on_delete=models.CASCADE, related_name='free_subcategories')
    about = models.TextField(blank=True, null=True, verbose_name="Batafsil")
    examp_type = models.CharField(max_length=20, choices=EXAMP_TYPE, default='always', verbose_name="Imtihon turi")

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ochiq Kichik kategoriya"
        verbose_name_plural = "Ochiq Kichik kategoriyalar"
        # ordering = ('-created_at',)

    def __str__(self):
        return self.name

def slug_funckion_for_free_result_model(self):
    """ Ikkita maydonni sludada birlashtirish """
    return f"{self.subcategory.name}-free-result"

class FreeResult(models.Model):
    subcategory = models.ForeignKey(FreeSubCategory, on_delete=models.CASCADE, related_name="free_results", blank=True, null=True)
    slug = AutoSlugField((u'slug'), populate_from=slug_funckion_for_free_result_model, unique=True)
    ball = models.PositiveIntegerField(default=0, blank=True, null=True)
    # answers - o'quvchining belgilagan javovblari yuboriladigan maydon
    answers = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ochiq Natija"
        verbose_name_plural = "Ochiq Natijalar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.subcategory.name
""" ---------------------------------------------------------------------- """


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)

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
    slug = AutoSlugField(populate_from='name', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    about = models.TextField(blank=True, null=True, verbose_name="Batafsil")
    examp_type = models.CharField(max_length=20, choices=EXAMP_TYPE, default='always', verbose_name="Imtihon turi")

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
    name = models.CharField(max_length=111)
    slug = AutoSlugField(populate_from = 'name',unique=True)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE,related_name='examp')
    main_examp = models.BooleanField(default=False, null=True, blank=True)
    about = models.TextField(blank=True, null=True, verbose_name="Batafsil")
    time = models.PositiveIntegerField(verbose_name='Vaqt',null=True)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Imtihon"
        verbose_name_plural = "Imtihonlar"
        # ordering = ['-created_at',]

    def __str__(self) -> str:
        return self.name

def slug_funckion_for_question_model(self):
    """ Ikkita maydonni sludada birlashtirish """
    return f"{self.question_text[:20]}"

class Question(models.Model):
    """ Imtihon va darsdan keyin beriladigan imtihon uchun savollar """
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    free_subcategory = models.ForeignKey(FreeSubCategory, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    examp = models.ForeignKey(Examp, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    question_text = models.CharField(max_length=123)
    slug = AutoSlugField((u'slug'), populate_from=slug_funckion_for_question_model, unique=True)
    
    status = models.BooleanField(default=True,)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"
        # ordering = ['created_at',]

    def __str__(self):
        return self.question_text

def slug_funckion_for_answer_model(self):
    """ Ikkita maydonni sludada birlashtirish """
    return f"{self.question.question_text[:15]} - {self.answer_text[:15]}"

class Answer(models.Model):
    """ Savol javoblari uchun models """
    question = models.ForeignKey(Question, related_name='answers',on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=221,verbose_name='Answer Text')
    slug = AutoSlugField((u'slug'), populate_from=slug_funckion_for_answer_model, unique=True)
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

def slug_funckion_for_result_model(self):
    """ Ikkita maydonni sludada birlashtirish """
    return f"{self.student.first_name}-result"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    slug = AutoSlugField((u'slug'), populate_from=slug_funckion_for_result_model, unique=True)
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

