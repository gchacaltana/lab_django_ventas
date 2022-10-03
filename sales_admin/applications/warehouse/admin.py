from django.contrib import admin

# Importamos los modelos que deseamos agregar al django admin
from applications.warehouse.models import UnitMeasureCategory
from applications.warehouse.models import UnitMeasure
from applications.warehouse.models import ProductCategory
from applications.warehouse.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Clase para personalizar cómo queremos trabajar con el modelo Product
    en Django admin.
    """

    # Definimos los atributos que queremos mostrar en django admin (formulario)
    fields = ('code', 'name', 'product_category_id', 'unit_measure_id',
              'currency_id', 'purchase_price', 'base_sale_price', 'percent_discount')
    
    # Definimos los atributos que queremos que se muestren en el listado de productos
    # display_sale_price: es una función que devuelve el precio de venta.
    list_display = ["code", "name", "product_category_id", "display_sale_price"]

    def display_sale_price(self, obj) -> str:
        """
        Método que devuelve el precio de venta del producto con el simbolo
        de la moneda.
        """
        return f"{obj.currency_id.symbol} {obj.sale_price}"

    # Defimos el nombre de la columna
    display_sale_price.short_description = "Precio de Venta"

# Agregamos al modelo UnitMeasureCategory al django admin
admin.site.register(UnitMeasureCategory)
admin.site.register(UnitMeasure)
admin.site.register(ProductCategory)
