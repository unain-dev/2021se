from django.shortcuts import render, redirect, get_object_or_404
from .models import product
# Create your views here.


def rings(request) :
   products_rings =product.objects.all().filter(category='rings')
   return render(request,'rings.html',{'products_rings':products_rings})

def glasses(request) :
   products_glasses =product.objects.all().filter(category='glasses')
   return render(request,'glasses.html',{'products_glasses':products_glasses})


def socks(request) :
   products_socks =product.objects.all().filter(category='socks')
   return render(request,'socks.html',{'products_socks':products_socks})

def necklace(request) :
   products_necklace =product.objects.all().filter(category='necklace')
   return render(request,'necklace.html',{'products_necklace':products_necklace})
 