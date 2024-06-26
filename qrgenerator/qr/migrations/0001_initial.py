# Generated by Django 5.0.4 on 2024-05-18 05:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Qr",
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
                ("title", models.CharField(max_length=75)),
                ("body", models.TextField()),
                ("slug", models.SlugField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("url", models.URLField(null=True)),
                (
                    "image",
                    models.ImageField(blank=True, default="fallback.png", upload_to=""),
                ),
            ],
        ),
    ]
