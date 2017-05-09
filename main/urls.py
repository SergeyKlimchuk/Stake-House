
from django.conf.urls import url, include
from django.contrib import admin

from main import views

urlpatterns = [
    url(r'^', views.about, name='main'),
    url(r'^about', views.about, name='about'),
    url(r'^beer', views.about, name='beer'),
    url(r'^contact', views.about, name='contact'),
    url(r'^food', views.about, name='food'),
    url(r'^reservation', views.about, name='reservation')
]
