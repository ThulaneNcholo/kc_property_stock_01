from django.shortcuts import render


# ============= Index View =============
def IndexView(request):
    context = {
        "page": "client/index.html",
    }

    if request.htmx:
        return render(request, "client/index.html", context)
    return render(request, "client/base.html", context)
