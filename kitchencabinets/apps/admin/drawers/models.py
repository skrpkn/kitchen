from django.db import models
from apps.admin.product.models import Product

class Drawers(models.Model):
    id = models.IntegerField(primary_key=True)
    drawer_name = models.CharField(max_length=45L, unique=True, blank=True)
    drawer_unit_price = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'drawers'
        
        
class ProductDrawers(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, null=True, blank=True)
    drawer = models.ForeignKey(Drawers, null=True, blank=True)
    product_drawers_quantity = models.IntegerField(null=True, blank=True)
    product_drawer_total_price = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'product_drawers'
