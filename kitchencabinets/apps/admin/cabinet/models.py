from django.db import models
from apps.admin.product.models import Product

class Cabinet(models.Model):
    id = models.IntegerField(primary_key=True)
    cabinet_name = models.CharField(max_length=45L, unique=True, blank=True)
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    class Meta:
        db_table = 'cabinet'

    
    

class ProductCabinetConstruction(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, null=True, blank=True)
    cabinet_construction = models.ForeignKey(Cabinet, null=True, blank=True)
    size = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'product_cabinet_construction'
