from django.urls import path, include

urlpatterns = [
    path('api/', include('products.urls')),  # Include product APIs
    path('api/', include('orders.urls')),    # Include order APIs
]
