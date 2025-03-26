from django.db import transaction
from products.models import Product
from .models import Order, OrderItem

def get_all_orders():
    """Retrieve all orders"""
    return Order.objects.all()

def create_order(items):
    """Handles business logic for order creation with stock validation"""
    if not items:
        raise ValueError("Order must contain at least one product.")

    with transaction.atomic():  # Ensures atomicity
        total_price = 0
        order = Order.objects.create(status="pending", total_price=0)

        for item in items:
            product_id = item.get("product")
            quantity = item.get("quantity")

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise ValueError(f"Product with ID {product_id} does not exist.")

            if quantity is None or quantity <= 0:
                raise ValueError(f"Invalid quantity for {product.name}.")

            if product.stock < quantity:
                raise ValueError(f"Not enough stock for {product.name}. Available: {product.stock}")

            # Deduct stock
            product.stock -= quantity
            product.save()

            # Create OrderItem
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        total_price += product.price * quantity
        # Update total price of the order
        order.total_price = total_price
        # order.status = "completed"
        order.save()

    return order
