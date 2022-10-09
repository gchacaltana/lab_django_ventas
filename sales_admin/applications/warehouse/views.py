from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from applications.warehouse.models import ProductCategory
from django.views.decorators.csrf import csrf_protect
from applications.warehouse.forms import ProductCategoryForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Vista Basada en Función.
    Función que devuelve página home del módulo de almacén.
    """
    return render(request, 'warehouse/index.html')

def product_category_list(request):
    """
    Función que devolverá la lista de categorías.
    Vista basada en función.
    """
    # link: https://docs.djangoproject.com/en/4.1/topics/db/queries/

    # Obtenemos los registros de la tabla product_category
    product_category_list = ProductCategory.objects.all().order_by('-id')

    # render(request, 'template.html',variables)
    return render(request, 'warehouse/product_category/list.html', {
        'product_category_list': product_category_list
    })


def detail(request, product_category_id):
    product_category = get_object_or_404(
        ProductCategory, pk=int(product_category_id))
    return render(request, "warehouse/product_category/detail.html", {
        "product_category": product_category
    })


def new(request):
    """
    Función que devuelve el formulario para agregar una nueva categoría de producto
    """
    form = ProductCategoryForm()
    return render(request, "warehouse/product_category/new.html", {
        'form': form
    })


def search(request):
    """
    Función para devolver template de búsqueda de categoría de producto.
    """
    return render(request, "warehouse/product_category/search.html", {})


@require_http_methods(["POST"])
@csrf_protect
def save(request):
    """
    Función para registrar los datos del formulario en la base de datos.
    """
    print(request.POST)
    form = ProductCategoryForm(request.POST)
    if form.is_valid():
        try:
            code = form.cleaned_data.get('code')
            name = form.cleaned_data.get('name')
            percent_discount = form.cleaned_data.get('percent_discount')
            pc = ProductCategory(code=code, name=name,
                                 percent_discount=percent_discount)
            pc.save()
            return render(request, 'warehouse/product_category/new.html', {'form': form})
            # return HttpResponse("Categoría creada con éxito")
        except Exception as e:
            return HttpResponse(e)
    else:
        print(form.errors)
        return render(request, 'warehouse/product_category/new.html', {'form': form})
