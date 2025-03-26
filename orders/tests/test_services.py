from django.test import TestCase
from orders.services import create_order
from products.models import Product


class OrderServiceTestCase(TestCase):
    """Unit tests for order business logic in orders/services.py."""

    def setUp(self):
        self.product = Product.objects.create(
            name="Headphones", description="Wireless headphones", price=150, stock=5
        )

    def test_order_stock_deduction(self):
        """Ensure stock is correctly deducted when placing an order using the service."""
        order = create_order([{"product": self.product.id, "quantity": 3}])
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 2)
        self.assertEqual(order.total_price, 450)

    def test_order_insufficient_stock_service(self):
        """Ensure service raises error when trying to order more than available stock."""
        with self.assertRaises(ValueError):
            create_order([{"product": self.product.id, "quantity": 10}])

    def test_order_invalid_product_service(self):
        """Ensure service raises error when using an invalid product ID."""
        with self.assertRaises(ValueError):
            create_order([{"product": 9999, "quantity": 1}])
