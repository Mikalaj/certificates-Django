'''
Created on 19 апр. 2018 г.

@author: Мікалай
'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
]