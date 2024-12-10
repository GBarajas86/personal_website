from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_page_view(request):
    return HttpResponse("Pagina de inicio")


def about_page_view(request):
    context = {"name": "Gualberto", "age": 38}
    return render(request, "pages/about.html", context)


def contact_page_view(request):
    context = {"email" : "gualbarajas1986@gmail.com", "telephone": 9711179604}
    return render(request, "pages/contact.html", context)