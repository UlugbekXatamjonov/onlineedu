# Generated by Django 4.2.1 on 2023-05-19 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("exam", "0002_alter_examp_options_examp_created_at_examp_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="answer",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Javob",
                "verbose_name_plural": "Javoblar",
            },
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "Kategoriya",
                "verbose_name_plural": "Kategoriyalar",
            },
        ),
        migrations.AlterModelOptions(
            name="examp",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Imtihon",
                "verbose_name_plural": "Imtihonlar",
            },
        ),
        migrations.AlterModelOptions(
            name="question",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Savol",
                "verbose_name_plural": "Savollar",
            },
        ),
        migrations.AlterModelOptions(
            name="subcategory",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "Kichik kategoriya",
                "verbose_name_plural": "Kichik kategoriyalar",
            },
        ),
        migrations.CreateModel(
            name="Result",
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
                (
                    "examp",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="exam.examp",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="exam.subcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Natija",
                "verbose_name_plural": "Natijalar",
                "ordering": ["-created_at"],
            },
        ),
    ]
