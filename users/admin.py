""" Users admin config """

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    # informacion a mostrar
    list_display=('id','user','birthdate','website','picture')

    # Elementos clickeables
    list_display_links=('id','user')

    # Elementos editables ahi mismo
    list_editable=('birthdate','website')

    # Buscar elementos
    search_fields=('user__email','user__is_staff','created','modified')
