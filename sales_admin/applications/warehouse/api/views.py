from rest_framework.viewsets import ModelViewSet, ViewSet
from applications.warehouse.models import ProductCategory
from applications.warehouse.api.serializers import ProductCategorySerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

class ProductCategoryViewSet(ModelViewSet):
    """
    Clase ViewSet de Product Category
    """

    # Obtenemos los datos que queremos devolver.
    queryset = ProductCategory.objects.all()

    # Le indicamos el serializer que debe utilizar para convertir los objetos a JSON.
    serializer_class = ProductCategorySerializer

    # Configuración para que el VIEW sea utilizado por usuarios autenticados.
    #permission_classes = [IsAuthenticated]