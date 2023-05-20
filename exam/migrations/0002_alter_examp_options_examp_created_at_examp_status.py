# Generated by Django 4.2.1 on 2023-05-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="examp",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="examp",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="examp",
            name="status",
            field=models.BooleanField(default=True),
        ),
    ]
