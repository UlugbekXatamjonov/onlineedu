from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.utils.html import mark_safe

from autoslug import AutoSlugField

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
    def create_user(self, username, first_name, last_name,  email, age, gender, phone,
                    password=None, password2=None, ball=0, coin=0,):

        if not username:
            raise ValueError("Foydalanuvchida 'username' bo'lishi shart !")
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,
            gender=gender,
            phone=phone,
            ball = ball,
            coin =coin

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):

        user = self.create_user(
            password=password,
            username=username,
            email=email,
            first_name='Admin',
            last_name='Admin',
            age=1,
            gender='man',
            ball = 0,
            coin = 0,
            phone='998991234567'
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Student(AbstractUser):
    """ O'quvchi modeli """
    username = models.CharField(max_length=51, unique=True, verbose_name="username")
    slug = AutoSlugField(populate_from='username', unique=True)
    age = models.PositiveIntegerField(verbose_name="Yoshi")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=12, verbose_name='Tel. raqam')
    gender = models.CharField(max_length=10, choices=GENDER, default='man', verbose_name="Jinsi")
    ball = models.PositiveIntegerField(default=0, verbose_name="O'quvchining bali")
    coin = models.PositiveIntegerField(default=0, verbose_name="O'quvchining tangasi")

    objects = UserManager()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()


    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.username

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





