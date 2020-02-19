from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    the_user = models.OneToOneField(User, on_delete='CASCADE')

    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.the_user.username
