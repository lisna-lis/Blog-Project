from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    # Set the email field as the USERNAME_FIELD
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    profile_pic = models.ImageField(upload_to='profile_pictures',null=True) 

    def  __str__(self):
        return self.email

    class Meta:
        ordering = ['-id']
        verbose_name =  'Profile'
        verbose_name_plural = 'Profiles'

