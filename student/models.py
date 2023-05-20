from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.utils.html import mark_safe

from autoslug import AutoSlugField

from course.models import Course

# Create your models here.

GENDER = (
    ('man',"Erkak"),
    ('woman',"Ayol"),
)

STATUS = (
    ('active', "Faol"),
    ("deactive", "Faol emas"),
)

_validate_phone = RegexValidator(
    regex=r"^[\+]?[9]{2}[8]?[0-9]{2}?[0-9]{3}?[0-9]{2}?[0-9]{2}$",
    message="Telefon raqamingiz 9 bilan boshlanishi va 12 belgidan oshmasligi lozim. Masalan: 998334568978",
)

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name,  email, phone,
                    password=None, password2=None, ball=0, coin=0,):

        if not email:
            raise ValueError("Foydalanuvchida 'email' bo'lishi shart !")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            ball = ball,
            coin =coin

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):

        user = self.create_user(
            password=password,
            email=email,
            first_name='Admin',
            last_name='Admin',
            ball = 0,
            coin = 0,
            phone='998991234567'
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Student(AbstractUser):
    """ O'quvchi modeli """
    email = models.EmailField(unique=True, verbose_name="Email")
    slug = AutoSlugField(populate_from='email', unique=True)
    phone = models.CharField(max_length=20, verbose_name='Tel. raqam')
    ball = models.PositiveIntegerField(default=0, verbose_name="O'quvchining bali")
    coin = models.PositiveIntegerField(default=0, verbose_name="O'quvchining tangasi")

    objects = UserManager()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now=True)

    # username - kerak emas bu loyihada
    username = None
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

class MyCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='my_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ball = models.PositiveIntegerField(default=0)
    coin = models.PositiveIntegerField(default=0)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mening kursim"
        verbose_name_plural = "Mening kurslarim"

    def __str__(self):
        return f"{self.course.name}"

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    comment = models.TextField()

    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Xabar")
        verbose_name_plural = ("Xabarlar")
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


