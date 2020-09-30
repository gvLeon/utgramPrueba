""" Post Models """

from django.db import models
from users.models import Profile

# Create your models here.
class Post (models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    # Required pillow library
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

