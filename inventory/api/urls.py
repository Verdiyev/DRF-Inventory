from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('product-list/', views.productList, name='product-list'),
    path('order-list/', views.orderList, name='order-list'),
    path('product-create/', views.productCreate, name='product-create'),
    path('product-update/<int:pk>', views.productUpdate, name='product-update'),
    path('order-create/', views.orderCreate, name='order-create'),

    path("products/", views.ProductList.as_view(), name="product_list"),
    path("orders/", views.OrderList.as_view(), name="order_list"),
    path("orderproducts/", views.OrderProductList.as_view(), name="order_list"),

    path("orderproducts/<int:pk>", views.OrderProductDetail.as_view(), name="order_list"),
    path("orders/<int:pk>", views.OrderDetail.as_view(), name="order_list"),
    path("products/<int:pk>/", views.ProductDetail.as_view(), name="product_detail"),
    
    path("reports/", views.ReportListView.as_view(), name="report_list"),
    
   

]