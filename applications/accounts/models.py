from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField('Email', unique=True, null=True)
    first_name = models.CharField('First name', max_length=30, unique=True)
    last_name = models.CharField('Last name', max_length=30)
    city = models.CharField(verbose_name='Город', max_length=255)

    USERNAME_FIELD = 'first_name'

    def __str__(self):
        return self.first_name