from django.test import TestCase
from api.models import Product, OrderProduct, Order
from datetime import date

class ProductTest(TestCase):
    """ Test module for Product model """
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            product_name='tomato', cost=1.0, price = 1.2, qty_left = 1200)
        Product.objects.create(
            product_name='onion', cost=2.2, price = 3.0, qty_left = 500)


    def test_product_cost(self):
        product_tomato = Product.objects.get(id=1)
        product_onion = Product.objects.get(id=2)
        self.assertEqual(
            product_tomato.cost, 1.0)
        self.assertEqual(
            product_onion.cost, 2.2)
    
    def test_product_price(self):
        product_tomato = Product.objects.get(id=1)
        product_onion = Product.objects.get(id=2)
        self.assertEqual(
            product_tomato.price, 1.2)
        self.assertEqual(
            product_onion.price, 3.0)

    def test_product_qty_left(self):
        product_tomato = Product.objects.get(id=1)
        product_onion = Product.objects.get(id=2)
        self.assertEqual(
            product_tomato.qty_left, 1200)
        self.assertEqual(
            product_onion.qty_left, 500)


class OrderTest(TestCase):
    """ Test module for Order model """
    @classmethod
    def setUpTestData(cls):
        Order.objects.create(status = 'created', created_at=date(2022,3,25)
            )

    def test_order_status(self):
        order=Order.objects.get(id=1)
        self.assertEqual(
            order.status, 'created'
        )

class OrderProductTest(TestCase):
    """ Test module for OrderProduct model """
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            product_name='onion', cost=2.2, price = 3.0, qty_left = 500)
        Order.objects.create(status = 'created', created_at=date(2022,3,25)
            )
        OrderProduct.objects.create(
            product= Product.objects.get(id=1), order=Order.objects.get(id=1), 
                qty = 200)
      
    def test_orderproduct_units(self):
        op_200=OrderProduct.objects.get(id=1)
        self.assertEqual(
            op_200.qty, 200
        )
