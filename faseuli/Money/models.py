from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
# Create your models here.

class Money(models.Model):
    #user=models.CharField(max_length=50)
    cost=models.PositiveIntegerField()
    goal=models.PositiveIntegerField()
    percent=models.FloatField(null=True, default=0)

    def __str__(self):
        percent=cost/goal*100
        return self.goal

class History(models.Model):
    date=DateField(auto_now_add=True)
    cost=models.PositiveIntegerField()
    Money=models.ForeignKey(Money, on_delete=models.CASCADE, related_name='history')