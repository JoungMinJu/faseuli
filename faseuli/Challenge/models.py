from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.contrib.auth.models import User
import sys
sys.path.append("..")
from django.conf import settings


# Create your models here.
class Challenge(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="작성자", default="")
    #작성자
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