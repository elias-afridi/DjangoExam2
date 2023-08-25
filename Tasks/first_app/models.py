from django.db import models

# Create your models here.
class TaskModel(models.Model):
    Title=models.CharField(max_length=30)
    Description=models.CharField(max_length=100)
    Is_completed=models.BooleanField(default=False)
    