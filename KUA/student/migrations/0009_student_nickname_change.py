# Generated by Django 5.0.3 on 2024-07-04 02:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0008_alter_student_permission_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="nickname_change",
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]