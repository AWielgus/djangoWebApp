from django.shortcuts import render
from.models import History


def history_list(request, *args, **kwargs):
    my_context = {
        "list": History.objects.all()
    }
    return render(request, "history.html", my_context)
