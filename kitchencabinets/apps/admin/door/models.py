from django.db import models
from apps.admin.product.models import Product

        
class Doors(models.Model):
    door_id = models.AutoField(primary_key=True)
    door_name = models.CharField(unique=True, max_length=135, blank=True)
    door_price = models.CharField(max_length=135, blank=True)
    estimated_time = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'doors'


        
class ProductDoors(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product)
    door = models.ForeignKey(Doors)
    pieces_count = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'product_doors'

class DoorColors(models.Model):
    id = models.IntegerField(primary_key=True)
    door = models.ForeignKey(Doors)
    color_code = models.TextField()
    class Meta:
        db_table = u'door_colors'
