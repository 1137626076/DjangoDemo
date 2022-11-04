# Generated by Django 4.1.2 on 2022-11-04 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="user",
            fields=[
                (
                    "id",
                    models.AutoField(
                        max_length=11, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("username", models.CharField(max_length=255)),
                ("login_name", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("professional_class", models.CharField(max_length=225)),
            ],
            options={
                "db_table": "IOmember",
            },
        ),
    ]
