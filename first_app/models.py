from django.db import models

# Create your models here.

class TaskModel(models.Model):
    id= models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)
    status = models.CharField(max_length=30)
