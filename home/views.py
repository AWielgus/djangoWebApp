from django.shortcuts import render
from products.models import Product


def home_view(request):
    list = Product.objects.all()
    amountOfProduct = 0
    countOfProduct = 0
    valueOfWarehouse = 0
    for el in list:
        countOfProduct += 1
        amountOfProduct += el.amount
        valueOfWarehouse += el.amount*el.price
    my_context = {
        "p1": amountOfProduct,
        "p2": countOfProduct,
        "p3": valueOfWarehouse,
    }
    return render(request, "index.html", my_context)
