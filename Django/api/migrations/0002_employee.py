# Generated by Django 4.2.3 on 2023-07-14 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=100)),
                (
                    "work_type",
                    models.CharField(
                        choices=[
                            ("HR", "Human Resource"),
                            ("IT", "IT Support"),
                            ("Seale", "Seales Team"),
                            ("DI", "Directors"),
                            ("Own", "Owner"),
                        ],
                        max_length=50,
                    ),
                ),
                ("email", models.CharField(max_length=50, unique=True)),
                ("phone", models.CharField(max_length=13)),
                ("about", models.TextField(max_length=500)),
                (
                    "position",
                    models.CharField(
                        choices=[("Dev", "Developer"), ("Int", "Intern")], max_length=50
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.company"
                    ),
                ),
            ],
        ),
    ]