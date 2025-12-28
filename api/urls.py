from django.conf import  settings

from django.conf.urls.static import static
from django.urls import path
from .views import productview, product_detail
urlpatterns=[
    path('products/',productview,name='products'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)