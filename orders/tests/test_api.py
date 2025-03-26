from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from products.models import Product


class OrderAPITestCase(TestCase):
    """Test cases for Order API endpoints."""

    def setUp(self):
        self.client = APIClient()
        # Create a product to be used in orders
        self.product = Product.objects.create(
            name="Phone", description="Smartphone", price=500, stock=5
        )

    def test_create_order_success(self):
        """Test successfully placing an order and reducing stock."""
        order_data = {"items": [{"product": self.product.id, "quantity": 2}]}
        response = self.client.post("/api/orders/", order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 3)  # Stock should be reduced from 5 to 3

    def test_create_order_insufficient_stock(self):
        """Test order placement fails when ordered quantity exceeds stock."""
        order_data = {"items": [{"product": self.product.id, "quantity": 10}]}
        response = self.client.post("/api/orders/", order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_order_invalid_product(self):
        """Test order placement fails with an invalid product ID."""
        order_data = {"items": [{"product": 999, "quantity": 1}]}
        response = self.client.post("/api/orders/", order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
