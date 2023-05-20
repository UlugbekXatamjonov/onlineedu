# Generated by Django 4.2.1 on 2023-05-19 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
        ("student", "0006_alter_student_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="MyCourse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ball", models.PositiveIntegerField(default=0)),
                ("coin", models.PositiveIntegerField(default=0)),
                ("status", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("update_at", models.DateTimeField(auto_now_add=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="my_courses",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]