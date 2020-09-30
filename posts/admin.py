""" Post admin config """
# Django
from django.contrib import admin

# Models
from posts.models import Post

admin.site.register(Post)

# Register your models here.
