# Generated by Django 4.1.5 on 2023-01-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CrudUser",
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
                ("name", models.CharField(blank=True, max_length=30)),
                ("address", models.CharField(blank=True, max_length=100)),
                ("age", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
