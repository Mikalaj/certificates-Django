from django.shortcuts import render
from .models import Wedding

def index(request):
    return render(request, "certs/index.html", {})

def wedding(request, wedding_id):
    wedding = Wedding.objects.get(pk=wedding_id)
    return render(request, "certs/wedding.html", {'wedding': wedding})
    

# Create your views here.
