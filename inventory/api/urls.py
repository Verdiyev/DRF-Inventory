from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
   
    #Product APIs
    path("products/", views.ProductList.as_view(), name="product_list"),
    path("products/<int:pk>/", views.ProductDetail.as_view(), name="product_detail"),

    #Order APIs
    path("orders/", views.OrderList.as_view(), name="order_list"),
    path("orders/<int:pk>", views.OrderDetail.as_view(), name="order_detail"),

    #Order Product APIs
    path("orderproducts/", views.OrderProductList.as_view(), name="orderproduct_list"),
    path("orderproducts/<int:pk>", views.OrderProductDetail.as_view(), name="orderproduct_detail"),
    
    #Filtered Orders
    path("filtered_orders/", views.ReportListView.as_view(), name="report_list"),
    
   

]
