from django.contrib import admin
from .models import Dignity, Clergy, Baptism, Wedding

admin.site.register(Dignity)
admin.site.register(Clergy)
admin.site.register(Baptism)
admin.site.register(Wedding)

# Register your models here.
