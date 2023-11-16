# yourappname/models.py

from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Company(models.Model):
    user_baba = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=70)
    logo = models.ImageField(upload_to='company_logos/')  # Add this field for the company logo

    def __str__(self):
        return self.company
    


class Project(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True)
    project_name = models.CharField(max_length=100)
    main_contractor_name = models.CharField(max_length=100)
    plot_area = models.DecimalField(max_digits=50, decimal_places=2)
    built_up_area = models.DecimalField(max_digits=50, decimal_places=2)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name
    
class Photo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')  # 'photos/' is the upload directory

    def __str__(self):
        return f'Photo for {self.project.project_name}'
    



