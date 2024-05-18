from django.contrib import admin
from .models import *


admin.site.register(Authors)
admin.site.register(Languages)
admin.site.register(Genre)
admin.site.register(Books)