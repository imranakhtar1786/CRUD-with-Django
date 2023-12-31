# Generated by Django 4.2.6 on 2023-10-24 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="employee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                ("phone", models.CharField(max_length=11)),
                ("dsg", models.CharField(max_length=50)),
                ("salery", models.IntegerField()),
                (
                    "city",
                    models.CharField(blank=True, default="", max_length=50, null=True),
                ),
                (
                    "state",
                    models.CharField(blank=True, default="", max_length=50, null=True),
                ),
            ],
        ),
    ]
