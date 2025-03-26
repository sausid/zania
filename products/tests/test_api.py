from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from products.models import Product


class ProductAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            "name": "Laptop",
            "description": "A gaming laptop",
            "price": 1200.50,
            "stock": 10
        }
        # Create an initial product
        self.product = Product.objects.create(**self.product_data)

    def test_get_products(self):
        """Test retrieving all products."""
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check at least one product is returned
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_product_success(self):
        """Test creating a new product via API."""
        new_product = {
            "name": "Smartphone",
            "description": "Latest model smartphone",
            "price": 800,
            "stock": 15
        }
        response = self.client.post("/api/products/", new_product, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verify that the product was created
        self.assertEqual(Product.objects.filter(name="Smartphone").count(), 1)

    def test_create_product_invalid_price(self):
        """Test product creation failure with invalid (negative) price."""
        invalid_data = self.product_data.copy()
        invalid_data["price"] = -50
        response = self.client.post("/api/products/", invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)