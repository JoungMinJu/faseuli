from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField

# Create your models here.
class Challenge(models.Model):
    title=models.CharField(max_length=50)
    cost=models.PositiveIntegerField()
    goal=models.PositiveIntegerField()
    now=models.PositiveIntegerField(null=True, default=0)
    def __str__(self):
        return self.title

class History(models.Model):
    date=DateField(auto_now_add=True)
    cost=models.PositiveIntegerField()
    challenge=models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='history')