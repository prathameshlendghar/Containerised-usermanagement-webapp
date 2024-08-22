from django.db import models

# Create your models here.
class Employee(models.Model):
    GenderChoices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GenderChoices, default='M')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
