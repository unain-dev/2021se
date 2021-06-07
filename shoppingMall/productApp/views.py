from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import product,Photo,review
from cartApp import context_processors
from orderApp.models import Order,OrderItem
from django.utils import timezone
from django.db.models import Avg
# Create your views here.

def move_category(request, category):
   products_category =product.objects.all().filter(category=category)
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}
   return render(request,'view_product.html',{'products_category':products_category, 'count':count, 'category':category })

def product_detail(request,product_id):
   product_get=product.objects.filter(product_id=product_id)
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}

   photo_all=product.objects.all()
   photo_set=photo_all.filter(product_id=product_id)
   photo_get=Photo.objects.filter(product__in=photo_set)
   

   

   return render(request, 'detail.html',{'product_get':product_get, 'count':count, 'photo_get':photo_get})

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
         return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})

      elif min is not None and max=="": #상품명, 최소값
         products=product.objects.filter(name__contains=search_name)&product.objects.filter(price__range=(min, 1000000))&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})
      elif min=="" and max is not None: # 상품명, 최대값
         products=product.objects.filter(name__contains=search_name)&product.objects.filter(price__range=(0, max))&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})
      elif min is not None and max is not None: #상품명, 최소값, 최대값
         products=product.objects.filter(name__contains=search_name)&product.objects.filter(price__range=(min, max))&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})

    #상품명 제외하고 검색
   else:
      if min: #min 입력이 있을 때
         if max=="": #min만 가지고 검색
            products=product.objects.filter(price__range=(min, 1000000))&product.objects.all().filter(category=search_cateogry)
            return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})
         elif max: #min, max 가지고 검색
            products=product.objects.filter(price__range=(min, max))&product.objects.all().filter(category=search_cateogry)
            return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})

      elif max: #max만 입력 있을 때
         products=product.objects.filter(price__range=(0, max))&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})
      else: #아무것도 없을 때
         msg="아무것도 입력하지 않았습니다."
         return render(request, 'search_rings.html', {'msg':msg, 'count':count, 'category':search_cateogry})


def review_post(request,pk):

    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}
    
    order_items=OrderItem.objects.filter(pk=pk)
    return render(request,"review_post.html", {'count':count,'order_items':order_items})


def review_save(request):
    
 
     cart_count=context_processors.counter(request)
     cart_count=int(cart_count)
     count={'cart_count':cart_count}
     

     

     uid=request.session.get('user_id')
     p_id=request.POST['p_id']
     product_get=product.objects.filter(product_id=p_id)
    
     
     new_review=review()
     new_review.r_product=product.objects.get(product_id=p_id)
     new_review.r_stage=request.POST.get("r_stage")
     new_review.shipping_score=request.POST.get("shipping_score")
     new_review.r_content=request.POST['content']
     new_review.total_score=request.POST.get("total_score")
     new_review.r_user_id=uid

     new_review.save()
    
    

     return render(request,"review_board.html", {'product_get':product_get,'count':count})

def review_view(request,product_id):
    product_get=product.objects.filter(product_id=product_id)
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    review_all=product.objects.all()
    review_set=review_all.filter(product_id=product_id)
    review_get=review.objects.filter(r_product__in=review_set)
    p_avg_score=review_get.aggregate(Avg('total_score'))
    review_set.avg_score=p_avg_score
    
   
    return render(request,"review_board.html", {'p_avg_score':p_avg_score,'product_get':product_get,'count':count,'review_get':review_get})

