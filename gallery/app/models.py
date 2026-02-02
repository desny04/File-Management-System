from django.db import models

# Create your models here.

class Users(models.Model):
    name=models.TextField()
    email=models.EmailField()
    password=models.TextField()

class Docs(models.Model):
    title=models.TextField()
    file=models.FileField(upload_to='uploads/')
