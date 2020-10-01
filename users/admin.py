""" Users admin config """
# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    # Que es lo que quiero que se muestre
    list_display = ('id', 'user', 'birthdate', 'website', 'picture')
    # Que elementos son clickables
    list_display_links = ('id', 'user')
    # Que elementos se pueden editar ahi mismo
    list_editable = ('birthdate', 'website', 'picture')
    # Como quieres buscar un elemento
    search_fields = ('user__email', 'user__is_staff', 'created', 'modified')
    # Filtro de datos
    list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')


class ProfileInline(admin.StackedInline):
    """ Profile in-line admin for users """

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin """

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
    list_editable=('is_active', 'is_staff')

admin.site.unregister(User)
admin.site.register(User,UserAdmin)