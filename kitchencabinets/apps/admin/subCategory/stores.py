from lib.dojango.data.modelstore.stores import Store
from lib.dojango.data.modelstore.fields import StoreField
from lib.dojango.data.modelstore.methods import ObjectMethod



        
class CodesStore(Store):
    id=StoreField()
    code_group=StoreField()
    code_value=StoreField()
    
    class Meta(object):        
        identifier = 'id'
        label    = 'code_value' 