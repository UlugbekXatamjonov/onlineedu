# Generated by Django 4.2.1 on 2023-05-16 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0004_remove_student_age_remove_student_gender_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="username",
        ),
    ]
