# Generated by Django 5.0.2 on 2024-02-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="facts",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("fact", models.CharField(max_length=255)),
            ],
        ),
    ]
