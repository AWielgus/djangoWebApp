from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product


def home_view(request, *args, **kwargs):
    list = Product.objects.all()
    amountOfProduct = 0
    countOfProduct = 0
    valueOfWarehouse = 0
    countOfDeleted = 0
    for el in list:
        if el.hidden:
            countOfDeleted += 1
        else:
            countOfProduct += 1
            amountOfProduct += el.amount
            valueOfWarehouse += el.amount*el.price
    my_context = {
        "p1": amountOfProduct,
        "p2": countOfProduct,
        "p3": valueOfWarehouse,
        "p4": countOfDeleted,
    }
    return render(request, "index.html", my_context)
