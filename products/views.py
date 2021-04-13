from django.shortcuts import render
from .models import Product

# Create your views here.


def all_wines(request):
    """ A view to show all wines """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def wine_detail(request, product_id):
    """ A view to show individual wine bottles details """

    product = get_obejct_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/wine_details.html', context)
