# Generated by Django 5.0.3 on 2024-04-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0002_remove_student_last_login_remove_student_password"),
    ]

    operations = [
        migrations.CreateModel(
            name="Email",
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
                ("email", models.CharField(max_length=30, unique=True)),
                ("permission_code", models.CharField(default="", max_length=8)),
            ],
        ),
    ]
