''' Users views '''

# Django
# Libreria para ayudarnos a hacer el login del usuario y 'login' para manejar la sesion del usuario por ej al cambiar de pestana se queda la sesion iniciada
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Models
from users.models import Profile 

# Exception
from django.db.utils import IntegrityError



def login_view(request):
    '''Login view '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'Usuario o contrasena invalido!'})

    return render(request,'users/login.html')

@login_required
def logout_view(request):
    '''Logout a user '''
    logout(request)
    return redirect('login')

def signup(request):
    '''Sign up view'''
    if request.method == 'POST':
        username = request.POST['username']

        password = request.POST['passwd']
        password_confirm = request.POST ['passwd_confirmation']
        if password != password_confirm:
            return render(request,'users/signup.html', {'error':'Las contrasenas no coinciden'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request,'users/signup.html', {'error':'El nombre de usuario ya existe'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request,'users/signup.html')

@login_required
def update_profile(request):
    """ Update a user's profile view """
    return render(request, 'users/update_profile.html')
        
