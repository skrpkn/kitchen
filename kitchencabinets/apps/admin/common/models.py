from django.db import models


class Codes(models.Model):
    id = models.IntegerField(primary_key=True)
    code_group = models.CharField(max_length=135, blank=True)
    code_value = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'codes'
            
