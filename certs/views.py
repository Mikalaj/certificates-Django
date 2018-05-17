from django.shortcuts import render
from .models import Wedding, Baptism
from django.contrib.auth.models import User, Group
from rest_framework import viewsets


def index(request):
    return render(request, "certs/index.html", {})


def home(request):
    return render(request, "home.html", {})


def wedding(request, wedding_id):
    wedding = Wedding.objects.get(pk=wedding_id)
    return render(request, "certs/wedding.html", {'wedding': wedding})


def baptism(request, baptism_id):
    baptism = Baptism.objects.get(pk=baptism_id)
    return render(request, "certs/baptism.html", {'baptism': baptism})
