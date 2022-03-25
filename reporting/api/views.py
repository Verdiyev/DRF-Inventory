from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import Order
from .serializers import OrderSerializer


@api_view(['GET', ])
def apiOverview(request):
    api_urls = {
        'Get metrics in date range' : 'POST /metrics/',
    }
    return Response(api_urls)

@api_view(['POST'])
def report(request):
    orders = Order.objects.filter(created_at__range=[request.data['start_date'], request.data['end_date']])
    serializer = OrderSerializer(orders, many = True)
    completed = orders.filter(status='completed')
    canceled = orders.filter(status='canceled')
    items_canceled = 0
    items_sold = 0
    profit = 0
    revenue = 0
    for order in canceled:
        order_products = order.order_products.all()
        for op in order_products:
            items_canceled += op.qty
    for order in completed:
        order_products = order.order_products.all()
        for op in order_products:
            items_sold += op.qty
            profit += op.qty * (op.product.price - op.product.cost)
            revenue += op.qty * (op.product.price)
    response = {   "revenue" : revenue,
                        "profit" : profit,
                        "items_sold" : items_sold,
                        "items_canceled" : items_canceled,
    }
    return Response(response)
    