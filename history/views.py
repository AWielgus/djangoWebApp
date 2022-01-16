from django.shortcuts import render


def history_list(request, *args, **kwargs):
    my_context = {
        "list": {12, 32, 321, 123, 123, 123, 12}
    }
    # return HttpResponse("<h1>hello world</h1>")
    return render(request, "history.html", my_context)
