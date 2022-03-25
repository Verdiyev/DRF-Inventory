from rest_framework import serializers
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
import json

from api.models import Product, OrderProduct, Order
from api.serializers import ProductSerializer, OrderProductSerializer

# initialize the APIClient app
client = Client()

class GetAllProductsTest(TestCase):
    """ Test module for GET all products """

    def setUp(self):
        Product.objects.create(
            product_name='tomato', cost=1.0, price = 1.2, qty_left = 1200)
        Product.objects.create(
            product_name='onion', cost=2.2, price = 3.0, qty_left = 500)
        Product.objects.create(
            product_name='potato', cost=0.6, price = 1.0, qty_left = 2300)
        Product.objects.create(
            product_name='garlic', cost=3.5, price = 5, qty_left = 250)

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('product_list'))
        # get data from db
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleProductTest(TestCase):
    """ Test module for GET single product """

    def setUp(self):
        self.tomato = Product.objects.create(
            product_name='tomato', cost=1.0, price = 1.2, qty_left = 1200)
        self.onion = Product.objects.create(
            product_name='onion', cost=2.2, price = 3.0, qty_left = 500)
        self.potato = Product.objects.create(
            product_name='potato', cost=0.6, price = 1.0, qty_left = 2300)
        self.garlic = Product.objects.create(
            product_name='garlic', cost=3.5, price = 5, qty_left = 250)

    def test_get_valid_single_product(self):
        response = client.get(
            reverse('product_detail', kwargs={'pk': self.tomato.pk}))
        product = Product.objects.get(pk=self.tomato.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(
            reverse('product_detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProductTest(TestCase):
    """ Test module for inserting a new product """

    def setUp(self):
        self.valid_payload = {
            'product_name': 'tomato',
            'cost': 1.0,
            'price' : 3.0, 
            'qty_left' : 500
        }
        self.invalid_payload = {
            'product_name': '',
            'cost': 1.2,
            'price' : 4.0, 
            'qty_left' : 1500
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('product_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            reverse('product_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleProductTest(TestCase):
    """ Test module for updating an existing product record """

    def setUp(self):
        self.tomato = Product.objects.create(
            product_name='tomato', cost=1.0, price = 1.2, qty_left = 1200)
        self.onion = Product.objects.create(
            product_name='onion', cost=2.2, price = 3.0, qty_left = 500)
        self.valid_payload = {
            'product_name': 'tomato',
            'cost': 1.0,
            'price' : 3.0, 
            'qty_left' : 500
        }
        self.invalid_payload = {
            'product_name': '',
            'cost': 1.0,
            'price' : 3.0, 
            'qty_left' : 500
        }

    def test_valid_update_product(self):
        response = client.put(
            reverse('product_detail', kwargs={'pk': self.tomato.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_product(self):
        response = client.put(
            reverse('product_detail', kwargs={'pk': self.tomato.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

