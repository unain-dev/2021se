from django.shortcuts import render, redirect, get_object_or_404
from .models import product
# Create your views here.
def product_list(request):
    products=get_object_or_404(product)
    

def rings(request) :
    return render(request, 'prdroductApp/rings.html',{'product':product})
 