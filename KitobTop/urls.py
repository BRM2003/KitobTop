from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from products.views import main_page

urlpatterns = [
    path("user/", include('users.urls')),
    path('', main_page, name='main_page')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)