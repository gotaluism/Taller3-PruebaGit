
from django.contrib import admin
from django.urls import path, include
from tienda import views 

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('',views.tienda, name='tienda'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)