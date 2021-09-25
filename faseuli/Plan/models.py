from django.db import models
from django.contrib.auth.models import User
import sys
sys.path.append("..")
from django.conf import settings


# Create your models here.
class Plan(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="작성자", default="")
    #작성자
    title=models.CharField(max_length=200)
    #제목
    goal=models.IntegerField(default=0)
    #비용
    image=models.ImageField(upload_to='images',blank=True, null=True)
    #이미지

    def __str__(self):
        return self.title
    class Meta:
        db_table='Plan'



class RecommendPlan(models.Model):
    title=models.CharField(max_length=200)
    #제목
    goal=models.CharField(max_length=200)
    #비용
    image=models.ImageField(upload_to='images',blank=True, null=True)
    #이미지
    HOBBY_CHOICE=(
        ('미술','미술'),
        ('레저','레저'),
        ('음악','음악'),
        ('공예','공예'),
        ('스포츠','스포츠'),
        ('재테크','재테크'),
        ('여행','여행'),
        ('사업','사업'),
    )
    hobby=models.CharField(max_length=20, choices=HOBBY_CHOICE,default='')
