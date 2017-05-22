
from django.conf.urls import url, include
from django.contrib import admin

from main import views

urlpatterns = [
    url(r'^about', views.about, name='about'),
    url(r'^beer', views.beer, name='beer'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^food', views.food, name='food'),
    url(r'^reservation', views.reservation, name='reservation'),
    url(r'^index2', views.index2),
    url(r'^', views.main, name='main')
]
