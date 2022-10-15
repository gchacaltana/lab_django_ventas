from rest_framework import routers
from applications.warehouse.api.views import ProductCategoryViewSet, GetProductCategoryWithToken, Logout
from django.urls import path
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('product-categories', ProductCategoryViewSet)
# router.register('products', ProductViewSet)

urlpatterns = [
    path("", include(router.urls), name="api-warehouse"),
    path("product-category/<int:id>/", GetProductCategoryWithToken.as_view(), name='get-product-category-token'),
    path("logout/", Logout.as_view(), name="logout")
]