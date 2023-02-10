

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30, blank=True)
    is_active = models.BooleanField('active', default=True)
    is_staff     = models.BooleanField('staff', default=True)
    is_verified    = models.BooleanField('verified', default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)




    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = ('username')
        verbose_name_plural =('users')

    def __str__(self):
        return self.email
    
    def token(self):
        return ''

  