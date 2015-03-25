from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    category_name = models.CharField(unique=True, max_length=135, blank=True)
    category_image = models.TextField(blank=True)
    category_order = models.IntegerField(unique=True, null=True, blank=True)
    category_status = models.CharField(max_length=45, blank=True)

    class Meta:
        db_table = u'category'

        
    def get_category_status(self):
        return self.category_status.code_value
    
    
