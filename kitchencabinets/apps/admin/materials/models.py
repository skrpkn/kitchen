from django.db import models

class Materials(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128L, unique=True)
    price = models.FloatField()
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15L)
    class Meta:
        db_table = 'materials'


   
    
