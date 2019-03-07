from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Category, Product
# Create your views here.


def allProdCat(request, c_slug=None):
    c_page= None
    products = None
    if c_slug == None:
        # c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=c_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'shop/category.html', {'category':c_page, 'products':products})
