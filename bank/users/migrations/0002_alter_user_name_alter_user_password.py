# Generated by Django 4.1.6 on 2023-02-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=15),
        ),
    ]
