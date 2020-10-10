from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# utilities
# Lib datetime de django
from datetime import datetime

# Create your views here.

posts = [
    {
        'title': 'Picture from Nietzy',
        'user': {
            'name': 'Nietzy Cardoza',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/300/300',
    },
    {
        'title': 'Picture from Crecencio',
        'user': {
            'name': 'Crecencio Gameros',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/300/300',
    },
    {
        'title': 'Picture from Brenda',
        'user': {
            'name': 'Brenda Gutierrez',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/300/300',
    },
    {
        'title': 'Picture from Luis',
        'user': {
            'name': 'Luis Hernandez',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/300/300',
    },
    {
        'title': 'Picture from Vianey',
        'user': {
            'name': 'Vianey Lopez',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/300/300',
    }
]

@login_required
def list_post (request):
    return render(request,'posts/feed.html',{'posts': posts})
