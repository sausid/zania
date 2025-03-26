from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ProductSerializer
from .services import create_product, get_all_products


class ProductViewSet(viewsets.ViewSet):
    """ViewSet for managing products"""

    def list(self, request):
        """Retrieve all available products"""
        products = get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new product"""
        try:
            product = create_product(request.data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
