from django.urls import path
from . import views

app_name = "warehouse"

urlpatterns = [
    path("", views.index, name = "home_warehouse"),
    # URL para categorías de producto
    path("categorias-producto",views.product_category_list, name = "product_category_list"),
    path("categorias-producto/<int:product_category_id>",views.detail, name = "product_category_detail"),
    path("categorias-producto/nuevo", views.new, name="product_category_new"),
    path("categorias-producto/buscar", views.search,name="product_category_search"),
    path("categorias-producto/guardar", views.save, name="product_category_save")
]
