from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 

#dummy data used as database

# posts = [
#     {
#         'author': 'Unnamed',
#         'title': 'Post 1',
#         'content': 'gvfghvfghsgvg',
#         'date': 'feb 29nd'
#     },
#     {
#         'author': 'Named',
#         'title': 'Post 2',
#         'content': 'gvfghvfghsgvg',
#         'date': 'june 21st'
#     }
# ]


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



