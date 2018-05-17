'''
Created on 19 апр. 2018 г.

@author: Мікалай
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('wedding/<int:wedding_id>', views.wedding, name="wedding"),
    path('baptism/<int:baptism_id>', views.baptism, name="baptism"),
]
