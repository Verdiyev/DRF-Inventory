from itertools import product
from rest_framework import serializers
from .models import Order, Product, OrderProduct
from rest_framework.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def update(self, instance, validated_data):
        instance.cost = validated_data.get('cost', instance.cost)
        instance.price = validated_data.get('price', instance.price)
        instance.qty_left = validated_data.get('qty_left', instance.qty_left)
        instance.save()
        return instance
class OrderProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderProduct
        fields = '__all__'

   
class OrderSerializer(serializers.ModelSerializer):
    order_product = OrderProductSerializer(many = True, required = False)
    class Meta:
        model = Order
        fields = '__all__'
        
    def update(self, instance, validated_data):
        #check if order is canceled
        if instance.status and instance.status == 'canceled':
            raise ValidationError("Order is canceled")
        #if not update the status
        instance.status = validated_data.get('status', instance.status)
        #check if order is being canceled and increase each product's available quantity
        if instance.status and instance.status == 'canceled':
            orderproducts = instance.order_products.all()
            for op in orderproducts:
                op.product.qty_left += op.qty
                op.product.save()
        instance.save()
        return instance
