from django.db import models

# Create your models here.# store/models.py

class Design_post(models.Model):
    design_title = models.CharField(max_length=255)
    design_catagories = models.CharField(max_length=255)
    Post_imageurl = models.URLField(null=True)
    create_at =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.design_title

class Designpost(models.Model):
    Details_imageurl = models.URLField(null=True)
    OverviewTitle = models.CharField(max_length=255)
    OverviewPara = models.TextField()
    ApproachTitle = models.CharField(max_length=255)
    ApproachPara = models.TextField()
    create_at =models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.Details_imageurl

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service_of_interest = models.CharField(max_length=100)
    timeline = models.DateField()
    project_details = models.TextField()

    def __str__(self):
        return self.name
