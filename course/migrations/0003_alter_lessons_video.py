# Generated by Django 4.2.1 on 2023-05-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_file_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lessons",
            name="video",
            field=models.URLField(blank=True, null=True),
        ),
    ]
