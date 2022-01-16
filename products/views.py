from django.shortcuts import render
from .models import Product


def product_list(request, *args, **kwargs):
    my_context = {
        "list": Product.objects.all(),
    }

    return render(request, "product/productList.html", my_context)
