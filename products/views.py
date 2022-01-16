from django.shortcuts import render
from .models import Product
from history.models import History
from datetime import datetime

def product_list(request):
    my_context = {
        "list": Product.objects.all(),
    }
    return render(request, "product/productList.html", my_context)


def product_add(request):
    if request.POST != {}:
        obj = Product()
        obj.name = request.POST['name']
        obj.price = request.POST['price']
        obj.amount = request.POST['amount']
        obj.description = request.POST['description']
        obj.save()
        history_obj = History()
        history_obj.product_name = obj.name
        history_obj.description = "Dodano produkt"
        history_obj.update_date= datetime.now()
        history_obj.save()
    context = {}
    return render(request, "product/productAdd.html", context)


def product_remove(request):
    obj = Product.objects.get(id=request.GET['id'])
    history_obj = History()
    history_obj.product_name = obj.name
    history_obj.description = "Usunieto produkt"
    history_obj.update_date = datetime.now()
    history_obj.save()

    obj.delete()
    my_context = {
        "list": Product.objects.all(),
    }
    return render(request, "product/productList.html", my_context)
