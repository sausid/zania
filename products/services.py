from .models import Product


def get_all_products():
    """Retrieve all products"""
    return Product.objects.all()


def create_product(data):
    """Business logic to create a product"""
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    if not name or not description:
        raise ValueError("Product name and description are required.")

    if price is None or price <= 0:
        raise ValueError("Price must be a positive number.")

    if stock is None or stock < 0:
        raise ValueError("Stock quantity cannot be negative.")

    return Product.objects.create(name=name, description=description, price=price, stock=stock)
