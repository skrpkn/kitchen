from django.db import models
from apps.admin.product.models import Product

class Hinges(models.Model):
    id = models.IntegerField(primary_key=True)
    hinges_name = models.CharField(max_length=45L, blank=True)
    hinges_unit_price = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'hinges'


        
    
class ProductHinges(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, null=True, blank=True)
    hinges = models.ForeignKey(Hinges, null=True, blank=True)
    hinges_min = models.IntegerField(null=True, blank=True)
    hinges_max = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'product_hinges'    
    
