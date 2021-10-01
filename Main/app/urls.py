from django.contrib import admin
from django.urls import path,include
from app import views


urlpatterns = [
    path('contact', views.contact,name="contact"),
    path('contactus.html', views.contact,name="contact1")
    
]
