# Generated by Django 5.0.3 on 2024-03-26 17:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("blog_title", models.CharField(max_length=50)),
                ("blog_text", models.TextField()),
                (
                    "blog_status",
                    models.CharField(
                        choices=[("Active", "Active"), ("Draft", "Draft")], max_length=6
                    ),
                ),
                (
                    "author_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
