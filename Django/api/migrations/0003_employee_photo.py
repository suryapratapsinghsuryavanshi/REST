# Generated by Django 4.2.3 on 2023-07-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_employee"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="photo",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
