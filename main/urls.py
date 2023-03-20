from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name='main'),
    path("contact_me", views.contact_me, name='contact_me'),
    path("contact", views.contact_me, name='contact'),
    
    
    
]