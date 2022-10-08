from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from applications.warehouse.models import ProductCategory
from django.views.decorators.csrf import csrf_protect
from applications.warehouse.forms import ProductCategoryForm
from django.http import HttpResponse

# Create your views here.


def index(request):
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
    form = ProductCategoryForm()
    return render(request, "warehouse/product_category/new.html", {
        'form': form
    })


def search(request):
    return render(request, "warehouse/product_category/search.html", {})


@require_http_methods(["POST"])
@csrf_protect
def save(request):
    """
    Función para registrar los datos del formulario
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
        except ValueError as e:
            return HttpResponse(e)
    else:
        print(form.errors)
        return render(request, 'warehouse/product_category/new.html', {'form': form})
