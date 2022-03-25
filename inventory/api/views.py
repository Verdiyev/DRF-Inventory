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
        'Create_Product' : '/product-create/',
        'Update_Product' : '/product-update/<int:pk>/',
        'List_Products' : '/product-list/',
        'List_Orders' : '/order-list/',
        'Create_Order' : '/order-create/',
        'Cancel_Order' : '/order-cancel/',
        'Get_Data' : '/get-data/<int:pk>/'

    }
    return Response(api_urls)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer    

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 

class OrderProductList(generics.ListCreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

class OrderProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

class ReportFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter(label="Date (Between)")
    
    class Meta:
        model = Order
        fields = ['created_at']

    
class ReportListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ReportFilter

    
    
        
 
    # {"start_date":"2022-03-20","end_date":"2022-03-25"}

# class ReportListView(generics.ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     filter_backends = [DateFromToRangeFilter]
#     filterset_fields = ['created_at']

@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def orderList(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data = request.data)
#error handling?
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request, pk):
    # if no model exists by this PK, raise a 404 error
    product = get_object_or_404(Product, pk=pk)
    
    if "product_name" in request.data:
        del request.data['product_name']
    serializer = ProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)         
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#TODO: initilize order and add orderproducts -> split into 2 methods 
@api_view(['POST'])
def orderCreate(request):
    serializer = OrderSerializer(data = request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



# @api_view(['POST'])
# def addToOrder(request, pk):
#     order = get_object_or_404(Order, pk=pk)
    

    # products = []
    # serializer = OrderSerializer(data = request.data)
    # if serializer.is_valid():
    #     print(serializer.save(),"----------------------------------------------")
    # for pr in request.data.get('products'):
    #     product = get_object_or_404(Product,pk=pr['id'])
    #     if product.qty_left < pr['qty']:
    #         raise exceptions.ValidationError(detail = 'not enough of ' + product.product_name)
    #     products.append(product)
    # # serializer = OrderSerializer(products, many = True)
    # return Response("SALAM")

#TODO: accumulate data based on creation of order 
@api_view(['GET'])
def getData(request, pk):
    return  Response("SALAM")


        # serializer = OrderProductSerializer()
#     serializer = OrderProductSerializer(data = request.data)
# #error handling?
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

#  {"status":"created",
# "products":[{"id":1, "qty":11},
#             {"id":2, "qty":22},
#             {"id":3, "qty":33}]}