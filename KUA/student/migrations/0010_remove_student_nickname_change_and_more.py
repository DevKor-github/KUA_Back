# Generated by Django 5.0.3 on 2024-07-04 02:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0009_student_nickname_change"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="nickname_change",
        ),
        migrations.AddField(
            model_name="student",
            name="nickname_change_time",
            field=models.DateTimeField(null=True),
        ),
    ]