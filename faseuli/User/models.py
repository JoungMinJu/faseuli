from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, nickname, password, hobby, age):
    
        user = self.model(
                username = username,
                nickname = nickname,
                hobby=hobby,
                age=age,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        
        

    def create_superuser(self, username, nickname, password, hobby, age):
        user = self.create_user(
            username = username,
                nickname = nickname,
                password=password,
                hobby=hobby,
                age=age,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, default='')
    nickname = models.CharField(max_length=100, unique=True, default='')
    hobby = models.CharField(max_length=50, default='')
    age = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "username"   
    REQUIRED_FIELDS= ["nickname", "hobby", "age"]

    def __str__(self):
        return self.username