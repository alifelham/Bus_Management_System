from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', views.login, name='blog-login'),
    path('payment/', views.payment, name='blog-payment'),
    path('booking/', views.booking, name='blog-booking'),
    path('edit-booking/', views.edit_booking, name='blog-edit-booking'),
    path('travel-packages/', views.travel_packages, name='blog-travel-packages'),
]
