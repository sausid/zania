from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Using a router for automatic URL handling
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
