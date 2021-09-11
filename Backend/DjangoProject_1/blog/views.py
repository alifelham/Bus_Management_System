from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 


def home(request):
    context = {
        #deafult title of page
        'title': 'home',
        #'posts': posts

        #gets all posts from the Post class
        #'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#def about(request):
#   return HttpResponse('<h1>Blog about</h1>')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



def login(request):
    return render(request, 'blog/login.html', {'title': 'Login'})

def payment(request):
    return render(request, 'blog/payment.html', {'title': 'Payment'})

def booking(request):
    return render(request, 'blog/booking.html', {'title': 'Booking'})

def edit_booking(request):
    return render(request, 'blog/edit_booking.html', {'title': 'Edit-Booking'})

def travel_packages(request):
    return render(request, 'blog/travel_packages.html', {'title': 'Travel-Packages'})
