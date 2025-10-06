from django.shortcuts import render


# ============= Index View =============
def IndexView(request):
    context = {
        "page": "client/index.html",
    }

    if request.htmx:
        return render(request, "client/index.html", context)
    return render(request, "client/base.html", context)


# ============= About Us View =============
def AboutUsView(request):
    context = {
        "page": "client/about.html",
    }

    if request.htmx:
        return render(request, "client/about.html", context)
    return render(request, "client/base.html", context)


# ============= Sellers View =============
def SellersView(request):
    context = {
        "page": "client/sellers.html",
    }

    if request.htmx:
        return render(request, "client/sellers.html", context)
    return render(request, "client/base.html", context)


# ============= Rentals View =============
def RentalView(request):
    context = {
        "page": "client/rentals.html",
    }

    if request.htmx:
        return render(request, "client/rentals.html", context)
    return render(request, "client/base.html", context)


# ============= Properties View =============
def PropertiesView(request):
    context = {
        "page": "client/properties.html",
    }

    if request.htmx:
        return render(request, "client/properties.html", context)
    return render(request, "client/base.html", context)


# ============= Services View =============
def ServicesView(request):
    context = {
        "page": "client/services.html",
    }

    if request.htmx:
        return render(request, "client/services.html", context)
    return render(request, "client/base.html", context)


# ============= Contact View =============
def ContactView(request):
    context = {
        "page": "client/contact.html",
    }

    if request.htmx:
        return render(request, "client/contact.html", context)
    return render(request, "client/base.html", context)
