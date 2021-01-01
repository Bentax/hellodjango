from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    header = "Personal Data"
    langs = ["English", "German", "Spanish"]
    user = {"name": "Tom", "age": 23}
    address = ("Baker-st.", 23, 23)

    data = {"header": header, "langs": langs, "user": user, "address": address}
    return render(request, "index.html", context=data)

def about(request):
    return TemplateResponse(request, "firstapp/home.html")

def contact(request):
    return HttpResponsePermanentRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")

def products(request, productid):
    category = request.GET.get("cat", ";kjgkgd")
    output = "<h2>Product N {0} Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
    return HttpResponse(output)