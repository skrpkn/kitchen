from django.db import models
from apps.admin.category.models import Category
from apps.admin.subCategory.models import SubCategory
from apps.admin.materials.models import Materials

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    cabinet = models.CharField(max_length=100L, blank=True)
    material = models.ForeignKey(Materials)
    category = models.ForeignKey(Category, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, null=True, blank=True)
    product_name = models.CharField(max_length=135, blank=True)
    product_code = models.CharField(max_length=135, blank=True)
    short_description = models.TextField(blank=True)
    descriptions = models.TextField(blank=True)
    product_price = models.FloatField(null=True, blank=True)
  #  tax = models.ForeignKey(Tax, null=True, blank=True)
    min_height = models.FloatField(null=True, blank=True)
    max_height = models.FloatField(null=True, blank=True)
    height_scale = models.FloatField(null=True, blank=True)
    min_width = models.FloatField(null=True, blank=True)
    max_width = models.FloatField(null=True, blank=True)
    width_scale = models.FloatField(null=True, blank=True)
    min_depth = models.FloatField(null=True, blank=True)
    max_depth = models.FloatField(null=True, blank=True)
    depth_scale = models.FloatField(null=True, blank=True)
    is_hinges = models.CharField(max_length=12)
    image = models.CharField(max_length=135, blank=True)
    is_door = models.CharField(max_length=12, blank=True)
    discount = models.FloatField(null=True, blank=True)
    is_drawer = models.CharField(max_length=12)
    video_url = models.CharField(max_length=200L, blank=True)
    is_custom = models.CharField(max_length=4L)

    class Meta:
        db_table = u'product'
        
class ImageMapping(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product)
    image_path = models.CharField(max_length=235)
    description = models.TextField()
    class Meta:
        db_table = u'image_mapping'




