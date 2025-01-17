# Generated by Django 5.1.3 on 2024-11-30 14:18

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("profiles", "0002_alter_profilemodel_country"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RatingModel",
            fields=[
                (
                    "primary_key_id",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "ratings",
                    models.IntegerField(
                        choices=[
                            (1, "Poor"),
                            (2, "Fair"),
                            (3, "Good"),
                            (4, "Very Good"),
                            (5, "Excellent"),
                        ],
                        default=0,
                    ),
                ),
                ("comments", models.TextField()),
                (
                    "agents",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="profiles.profilemodel",
                    ),
                ),
                (
                    "rating_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("agents", "rating_user")},
            },
        ),
    ]
