from django.test import TestCase

from products.services import create_product, get_all_products


class ProductServiceTestCase(TestCase):

    def test_create_product_success(self):
        """Test creating a product via the service function."""
        data = {
            "name": "Tablet",
            "description": "Android tablet",
            "price": 300,
            "stock": 8
        }
        product = create_product(data)
        self.assertIsNotNone(product.id)
        self.assertEqual(product.name, "Tablet")

    def test_create_product_invalid_data(self):
        """Test product service raises error with invalid data."""
        data = {
            "name": "",
            "description": "No name provided",
            "price": 300,
            "stock": 8
        }
        with self.assertRaises(ValueError):
            create_product(data)

    def test_get_all_products(self):
        """Test fetching all products via service function."""
        # Initially create two products
        create_product({
            "name": "Monitor",
            "description": "LED Monitor",
            "price": 200,
            "stock": 12
        })
        create_product({
            "name": "Keyboard",
            "description": "Mechanical keyboard",
            "price": 100,
            "stock": 20
        })
        products = get_all_products()
        self.assertGreaterEqual(len(products), 2)
