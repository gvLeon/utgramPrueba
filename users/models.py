""" Users Models """

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    """ Profile model
        Proxi model that extends data with other information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(
        upload_to = 'users/pictrues',
        blank= True,
        null = True
    )

    
    website = models.URLField(max_length = 255, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.user)