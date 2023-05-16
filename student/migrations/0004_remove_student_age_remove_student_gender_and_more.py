# Generated by Django 4.2.1 on 2023-05-16 07:52

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0003_alter_student_gender"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="age",
        ),
        migrations.RemoveField(
            model_name="student",
            name="gender",
        ),
        migrations.AlterField(
            model_name="student",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="email", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="username",
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
