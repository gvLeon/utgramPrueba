""" utgram URLs """
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# importando las vistas
from posts import views as posts_views

def hello_world(request):
    return HttpResponse('<h1>Hola mundosdasdasd</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),

    # PostViews
    path('feed/', posts_views.list_post)
]
