# Generated by Django 4.1.6 on 2023-02-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("banksite", "0002_alter_transfer_receiver_alter_transfer_sender"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transfer",
            name="receiver",
        ),
        migrations.RemoveField(
            model_name="transfer",
            name="sender",
        ),
        migrations.AddField(
            model_name="transfer",
            name="receiver",
            field=models.ManyToManyField(
                related_name="receiver", to="banksite.account"
            ),
        ),
        migrations.AddField(
            model_name="transfer",
            name="sender",
            field=models.ManyToManyField(related_name="sender", to="banksite.account"),
        ),
    ]