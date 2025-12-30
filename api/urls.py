from django.conf import  settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.urls import path
from .views import productview, product_detail,WorkerViewSet, signup_view
router= DefaultRouter()
router.register(r'workers', WorkerViewSet, basename='workers')

urlpatterns=[
    path('products/',productview,name='products'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('signup/', signup_view, name='signup'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+ router.urls