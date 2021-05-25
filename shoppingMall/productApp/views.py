from django.shortcuts import render, redirect, get_object_or_404
from .models import product
from cartApp import context_processors
# Create your views here.

def move_category(request, category):
   products_category =product.objects.all().filter(category=category)
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}
   return render(request,'view_product.html',{'products_category':products_category, 'count':count, 'category':category })

def rings(request) :
   products_rings =product.objects.all().filter(category='rings')
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}
   return render(request,'rings.html',{'products_rings':products_rings, 'count':count})

def product_detail(request,product_id):
   product_get=product.objects.filter(product_id=product_id)
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}

   return render(request, 'detail.html',{'product_get':product_get, 'count':count})

def glasses(request) :
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}
   products_glasses =product.objects.all().filter(category='glasses')
   return render(request,'glasses.html',{'products_glasses':products_glasses, 'count':count})


def necklace(request) :
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}
   products_necklace =product.objects.all().filter(category='necklace')
   return render(request,'necklace.html',{'products_necklace':products_necklace, 'count':count})

def hats(request) :
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}
   products_hats =product.objects.all().filter(category='hats')
   return render(request,'hats.html',{'products_hats':products_hats, 'count':count})

def search(request):
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}

   search_name=request.GET['search_name']
   min=request.GET['search_min']
   max=request.GET['search_max']
   search_cateogry=request.GET['search_cateogry']

   #상품명이 빈칸이 아닐때
   if search_name:
      if min=="" and max=="" : # 상품명으로 검색
         products=product.objects.filter(name__contains=search_name)&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count})

      elif min is not None and max=="": #상품명, 최소값
         products=product.objects.filter(name__contains=search_name)&product.objects.filter(price__range=(min, 1000000))&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count})
      elif min=="" and max is not None: # 상품명, 최대값
         products=product.objects.filter(name__contains=search_name)&product.objects.filter(price__range=(0, max))&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count})
      elif min is not None and max is not None: #상품명, 최소값, 최대값
         products=product.objects.filter(name__contains=search_name)&product.objects.filter(price__range=(min, max))&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count})

    #상품명 제외하고 검색
   else:
      if min: #min 입력이 있을 때
         if max=="": #min만 가지고 검색
            products=product.objects.filter(price__range=(min, 1000000))&product.objects.all().filter(category=search_cateogry)
            return render(request, 'search_rings.html', {'products':products, 'count':count})
         elif max: #min, max 가지고 검색
            products=product.objects.filter(price__range=(min, max))
            return render(request, 'search_rings.html', {'products':products, 'count':count})&product.objects.all().filter(category=search_cateogry)

      else: #min입력이 없을 때 = max만 입력 있을 때
         products=product.objects.filter(price__range=(0, max))
         return render(request, 'search_rings.html', {'products':products, 'count':count})&product.objects.all().filter(category=search_cateogry)