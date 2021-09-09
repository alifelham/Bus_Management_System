from django.contrib import admin
from .models import Post
# Register your models here.


#to show posts in the admin page 
admin.site.register(Post)
