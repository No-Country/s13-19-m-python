# Generated by Django 5.0.2 on 2024-02-21 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
