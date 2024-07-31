# Generated by Django 5.0.6 on 2024-07-31 02:43

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("course_id", models.CharField(max_length=20, unique=True)),
                ("course_name", models.CharField(max_length=50)),
                ("year", models.IntegerField()),
                ("semester", models.IntegerField()),
                ("instructor", models.CharField(max_length=30)),
                ("credits", models.IntegerField()),
                ("classification", models.CharField(max_length=10)),
                (
                    "course_week",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("월", "Monday"),
                                ("화", "Tuesday"),
                                ("수", "Wednesday"),
                                ("목", "Thursday"),
                                ("금", "Friday"),
                                ("토", "Saturday"),
                            ],
                            max_length=3,
                        ),
                        default=list,
                        size=7,
                    ),
                ),
                (
                    "course_period",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=django.contrib.postgres.fields.ArrayField(
                            base_field=models.IntegerField(), size=7
                        ),
                        default=list,
                        size=7,
                    ),
                ),
                (
                    "course_room",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        default=list,
                        null=True,
                        size=7,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "attached_file",
                    models.FileField(blank=True, null=True, upload_to="attachments/"),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="course.course",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="student.student",
                    ),
                ),
                ("tags", models.ManyToManyField(related_name="posts", to="course.tag")),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_chosen", models.BooleanField(default=False)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="student.student",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="course.post",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TimeTable",
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
                ("year", models.CharField(max_length=6)),
                ("semester", models.CharField(max_length=6)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timetables",
                        to="course.course",
                    ),
                ),
                (
                    "student",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timetables",
                        to="student.student",
                    ),
                ),
            ],
        ),
    ]
