from rest_framework.serializers import ModelSerializer
from applications.warehouse.models import ProductCategory

class ProductCategorySerializer(ModelSerializer):
    """
    Clase para convertir un objeto ProductCategory a un formato JSON.
    """
    class Meta:
        model = ProductCategory
        #fields = ['code','name','percent_discount']
        fields = '__all__'