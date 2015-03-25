from django.db import models
from apps.admin.common.models import Codes
from apps.admin.category.models import Category

class SubCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    sub_category_name = models.CharField(max_length=135, blank=True)
    sub_category_status = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'sub_category'