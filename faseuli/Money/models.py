from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
# Create your models here.
from django.contrib.auth.models import User
import sys
sys.path.append("..")
from django.conf import settings
from django.utils import timezone


class Money(models.Model):
    #user=models.CharField(max_length=50)
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="작성자", default="")
    #작성자
    cost=models.PositiveIntegerField()
    date=DateField(auto_now_add=True)

    def __str__(self):
        return self.goal
