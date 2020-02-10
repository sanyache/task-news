from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyUser(models.Model):
    """
    Extended User's model
    """
    ADMIN = ['Admin',]
    EDITOR = ['Editor',]
    CUSTOMUSER = ['Custom_user',]
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    birth_day = models.DateField()

    def __str__(self):
        return '{} {} {}'.format(self.user.first_name, self.user.last_name, self.user.username)
