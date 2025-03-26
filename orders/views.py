from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import OrderSerializer
from .services import create_order, get_all_orders


class OrderViewSet(viewsets.ViewSet):
    """ViewSet for managing orders"""

    def list(self, request):
        """Retrieve all orders"""
        orders = get_all_orders()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create an order after stock validation"""
        try:
            order = create_order(request.data.get("items", []))
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
