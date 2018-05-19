from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path('login/', views.login, name='login',
         kwargs={'template_name': 'accounts/login.html'}),
    path('logout/', views.logout, name='logout', kwargs={'next_page': '/certs/'}),
]
