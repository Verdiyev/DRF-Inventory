from itertools import product
from pyexpat import model
from django.db import models
from datetime import datetime


ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled')
)


class Product (models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length = 100)
    cost = models.FloatField()
    price = models.FloatField()
    qty_left = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return self.product_name 

class Order (models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='created')
    

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,  related_name='order_products' )
    qty = models.PositiveIntegerField(default = 1)

    def save(self, *args, **kwargs):
        if self.qty < self.product.qty_left:
            self.product.qty_left -= self.qty
            self.product.save()
            super(OrderProduct, self).save(*args, **kwargs)
        else:
                #do not save the order product
            return 
    
