# Generated by Django 5.1.6 on 2025-03-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nene", "0007_testimonial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="articles/"),
        ),
    ]
