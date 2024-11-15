from django.db import models

# Create your models here.# store/models.py

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service_of_interest = models.CharField(max_length=100)
    timeline = models.DateField()
    project_details = models.TextField()

    def __str__(self):
        return self.name
