from .models import Baptism, Wedding
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('baptism/', views.baptism_list, name="baptism_list"),
    path('baptism/create/', views.baptism_create, name="baptism_create"),
    path('baptism/<int:pk>/', views.baptism_detail, name="baptism_detail"),
    path('baptism/<int:pk>/edit/', views.baptism_update, name="baptism_edit"),
    path('baptism/<int:pk>/delete/', views.baptism_delete, name="baptism_delete"),

    path('wedding/', views.wedding_list, name="wedding_list"),
    path('wedding/create/', views.wedding_create, name="wedding_create"),
    path('wedding/<int:pk>/', views.wedding_detail, name="wedding_detail"),
    path('wedding/<int:pk>/edit/', views.wedding_update, name="wedding_edit"),
    path('wedding/<int:pk>/delete/', views.wedding_delete, name="wedding_delete"),
]

api_patterns = [
    path('api/baptism/', views.api_baptism_list),
    path('api/baptism/<int:pk>/', views.api_baptism_detail),
]

urlpatterns += api_patterns
