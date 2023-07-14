from django.db import models


# Create Company Model
class Company(models.Model):
    name = models.CharField(max_length=50)
    company_number = models.AutoField(primary_key=True)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(
        max_length=50,
        choices=(
            ("IT", "INFORMATION TECHNOLOGY"),
            ("NIT", "NON INFORMATION TECHNOLOGY"),
        ),
    )
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.location}"


# Create Employee Model
class Employee(models.Model):
    photo = models.ImageField(null=True, upload_to="./static/upload")
    name = models.CharField(max_length=100)
    work_type = models.CharField(
        max_length=50,
        choices=(
            ("HR", "Human Resource"),
            ("IT", "IT Support"),
            ("Seale", "Seales Team"),
            ("DI", "Directors"),
            ("Own", "Owner")
        )
    )
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=13)
    about = models.TextField(max_length=500)
    position = models.CharField(max_length=50, choices=(
        ("Dev", "Developer"),
        ('Int', "Intern")
    ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
