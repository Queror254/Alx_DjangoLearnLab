from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    followers = models.ManyToManyField('self',symmetrical=False,related_name='user_followers')
    following = models.ManyToManyField('self', symmetrical=False,related_name='user_following')
