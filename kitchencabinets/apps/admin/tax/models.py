from django.db import models
from apps.admin.category.models import Category
from apps.admin.product.models import Product

class Tax(models.Model):
    id = models.IntegerField(primary_key=True)
    tax_name = models.CharField(max_length=135, blank=True)
    tax_date = models.CharField(max_length=135, blank=True)
    tax_status = models.CharField(max_length=45, blank=True)
    tax_rate = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'tax'


class TaxRules(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    tax = models.ForeignKey(Tax, null=True, blank=True)
    tax_rule_status = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'tax_rules'

class TaxMapping(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product)
    tax = models.ForeignKey(Tax)
    class Meta:
        db_table = 'tax_mapping'