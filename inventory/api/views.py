from math import prod
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import exceptions, generics

from django_filters import rest_framework as filters


from .serializers import OrderSerializer, ProductSerializer, OrderProductSerializer
from .models import OrderProduct, Product, Order

@api_view(['GET', ])
def apiOverview(request):
    api_urls = {
        'List products' : 'GET /products/',
        'Product Detail' : 'GET /products/<int:pk>/',
        'Create Product' : 'POST /products/',
        'Update Product' : 'PUT /products/',
        'Create Order' : 'POST /orders/',
        'Cancel Order' : 'PUT /orders/<int:pk>/',
        'Create OrderProduct' : 'POST /orderproducts/',
    }
    return Response(api_urls)

# list Products
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# CRUD Product
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# list Orders
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer    

# CRUD Order
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 

# list OrderProducts
class OrderProductList(generics.ListCreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

# CRUD OrderProduct
class OrderProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

# filter date range 
class ReportFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter(label="Date (Between)")
    
    class Meta:
        model = Order
        fields = ['created_at']

# show orders in date period    
class ReportListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ReportFilter

