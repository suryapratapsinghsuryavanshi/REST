# Generated by Django 4.2.3 on 2023-07-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_employee_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="photo",
            field=models.ImageField(null=True, upload_to="./static/upload"),
        ),
    ]
