from django.urls import path
from . import views, api
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('auth/', drf_views.obtain_auth_token, name='auth'),
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

# API endpoints
api_patterns = [
    path('api/', api.api_root),
    path('api/baptism/',
         api.BaptismList.as_view(),
         name='baptism-list'),
    path('api/baptism/<int:pk>/',
         api.BaptismDetail.as_view(),
         name='baptism-detail'),
    path('api/wedding/',
         api.WeddingList.as_view(),
         name='wedding-list'),
    path('api/wedding/<int:pk>/',
         api.WeddingDetail.as_view(),
         name='wedding-detail'),
    path('api/clergy/',
         api.ClergyList.as_view(),
         name='clergy-list'),
    path('api/clergy/<int:pk>/',
         api.ClergyDetail.as_view(),
         name='clergy-detail'),
]

api_patterns = format_suffix_patterns(api_patterns)

urlpatterns += api_patterns
