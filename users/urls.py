from django.contrib import admin
from django.urls import path
from .views import *

admin.site.site_header = 'KitobTop Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path("authenticate/", authentication, name='authenticate')
    # path('profile')
]
