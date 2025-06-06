# Generated by Django 5.1.6 on 2025-03-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nene", "0006_alter_service_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
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
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Nom du client"),
                ),
                ("feedback", models.TextField(verbose_name="Témoignage")),
                (
                    "company",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Entreprise (optionnel)",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
