# Generated by Django 4.2.1 on 2023-05-22 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0006_alter_result_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="FreeResult",
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
                ("ball", models.PositiveIntegerField(blank=True, default=0, null=True)),
                ("answers", models.JSONField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "subcategory",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="free_results",
                        to="exam.subcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Free Natija",
                "verbose_name_plural": "Free Natijalar",
                "ordering": ("-created_at",),
            },
        ),
    ]
