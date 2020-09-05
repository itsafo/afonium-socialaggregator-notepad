# -*- encoding: utf-8 -*-
"""
THIS CREATE THE MODEL FOR THE APP USER
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='afoniumcore/static/assets/img/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


