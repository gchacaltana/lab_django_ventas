from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from applications.warehouse.models import ProductCategory
from applications.warehouse.api.serializers import ProductCategorySerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['percent_discount']

    search_fields = ['name']

    ordering_fields = ['id', 'percent_discount']

class GetProductCategoryWithToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, id = 0, *args, **kwargs):
        product_category = None

        req_user = request._user
        #print(req_user)
        have_permission = False
        if req_user.has_perm('warehouse.view_productcategory'):
            have_permission = True
            try:
                product_category = ProductCategory.objects.get(id=id)
            except ProductCategory.DoesNotExist:
                pass
        
        product_category_serializer = ProductCategorySerializer(
            product_category
        )

        payload = {
            'product_category': product_category_serializer.data,
            'have_permission': have_permission
        }

        return JsonResponse(payload)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)