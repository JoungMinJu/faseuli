from django.db import models

# Create your models here.
class Challenge(models.Model):
    title=models.CharField(max_length=50)
    cost=models.PositiveIntegerField()
    goal=models.PositiveIntegerField()
    now=models.PositiveIntegerField()