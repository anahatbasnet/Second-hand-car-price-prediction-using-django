# Generated by Django 4.1.7 on 2023-03-13 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predictcarmodel",
            name="year",
            field=models.IntegerField(),
        ),
    ]
