from django.db import models
from django.contrib.auth.models import User
from apps.admin.product.models import Product


class ShopingCart(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    class Meta:
        db_table = u'shoping_cart'
        
class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    cart_id = models.CharField(max_length=100L)
    user = models.ForeignKey(User)
    product_id = models.CharField(max_length=100L)
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()
    price = models.FloatField()
    quantity = models.IntegerField()
    class Meta:
        db_table = 'cart'


class OrderHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    cart_id = models.CharField(max_length=45L)
    check_out = models.IntegerField()
    class Meta:
        db_table = 'order_history'

