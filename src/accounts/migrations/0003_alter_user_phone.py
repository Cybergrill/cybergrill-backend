# Generated by Django 4.1.7 on 2023-03-13 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
