''' Users views '''

# Django
# Libreria para ayudarnos a hacer el login del usuario y 'login' para manejar la sesion del usuario por ej al cambiar de pestana se queda la sesion iniciada
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    '''Login view '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
