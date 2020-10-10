""" utgram URLs """
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Static files config
from django.conf import settings
from django.conf.urls.static import static

# importando las vistas
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    

    # PostViews
    path('posts/feed/', posts_views.list_post,name='feed'),

    # Users views
    path('users/login/', users_views.login_view, name='login'),
    path('users/login/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
