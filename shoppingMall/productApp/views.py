from datetime import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .models import product,Photo,review
from cartApp import context_processors
from orderApp.models import Order,OrderItem
from django.utils import timezone
from django.db.models import Avg
from django.core.paginator  import Paginator
from shoppingApp.models import UserAccounts
from shoppingApp.models import address as Address

# Create your views here.

def move_category(request, category):
   my_products=product.objects
   products_category =product.objects.all().filter(category=category)
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}

    
   paginator=Paginator(products_category,3)
   page=request.GET.get('page')
   p_posts=paginator.get_page(page)


   if request.method == 'POST':
      select_order=request.POST.get('select_order')
      if select_order == 'by_name':
         products_category =product.objects.all().filter(category=category).order_by('name')
      elif select_order == 'by_high_price':
         products_category =product.objects.all().filter(category=category).order_by('price')
      elif select_order == 'by_low_price':
         products_category =product.objects.all().filter(category=category).order_by('-price')
      elif select_order == 'by_recent':
         products_category =product.objects.all().filter(category=category).order_by('pubDate')
      
      paginator=Paginator(products_category,3)
      page=request.GET.get('page')
      p_posts=paginator.get_page(page)
      return render(request,'view_product.html',{'products_category':products_category,'p_posts':p_posts, 'count':count, 'category':category, 'select_order':select_order})

   return render(request,'view_product.html',{'my_products':my_products,'p_posts':p_posts,'products_category':products_category, 'count':count, 'category':category})

def product_detail(request,product_id):
   request.session['product_id']=product_id
   product_get=product.objects.filter(product_id=product_id)
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}

   photo_all=product.objects.all()
   photo_set=photo_all.filter(product_id=product_id)
   photo_get=Photo.objects.filter(product__in=photo_set)
#?????? ?????? ???
   try:
      product_set=product.objects.get(product_id=product_id)
      reviews=review.objects.filter(r_product=product_set)
      for re in reviews:
         re.r_user_id=re.r_user_id[:2]

      request.session['product_id']=product_id
      avg_score=reviews.aggregate(Avg('total_score'))
      for k, v in avg_score.items():
         p_avg_score=v
      p_avg_score=round(p_avg_score, 1)

      paginator=Paginator(reviews,5)
      page=request.GET.get('page')
      reviews=paginator.get_page(page)
      return render(request, 'detail.html',{'product_get':product_get, 'count':count, 'photo_get':photo_get, 'reviews':reviews, 'p_avg_score':p_avg_score})
      #??????, ?????? ?????? ???
   #?????? ?????? ???
   except:
      pass

   return render(request, 'detail.html',{'product_get':product_get, 'count':count, 'photo_get':photo_get})

'''
def product_detail_get_review(request):
   product_id=request.session.get('product_id')
   product_get=product.objects.filter(product_id=product_id)
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}

   photo_all=product.objects.all()
   photo_set=photo_all.filter(product_id=product_id)
   photo_get=Photo.objects.filter(product__in=photo_set)
   
   user=request.session.get('user_id')

   if user:
      account=UserAccounts.objects.get(user_id=user)
      product_set=product.objects.get(product_id=product_id)

   try:
      address=Address.objects.get(accounts=account, is_default=True)

      if review.objects.filter(r_product=product_set):
         reviews=review.objects.filter(r_product=product_set)

         for re in reviews:
            re.r_user_id=re.r_user_id[:2]

         request.session['product_id']=product_id
         avg_score=reviews.aggregate(Avg('total_score'))
         for k, v in avg_score.items():
            p_avg_score=v
         p_avg_score=round(p_avg_score, 1)

         paginator=Paginator(reviews,5)
         page=request.GET.get('page')
         reviews=paginator.get_page(page)
         return render(request, 'detail.html',{'product_get':product_get, 'count':count, 'photo_get':photo_get, 'address':address, 'reviews':reviews, 'p_avg_score':p_avg_score})
      else:
         return render(request, 'detail.html',{'product_get':product_get, 'count':count, 'photo_get':photo_get, 'address':address})

   except ObjectDoesNotExist:
      if review.objects.filter(r_product=product_set):
         reviews=review.objects.filter(r_product=product_set)

         for re in reviews:
            re.r_user_id=re.r_user_id[:2]

         request.session['product_id']=product_id
         avg_score=reviews.aggregate(Avg('total_score'))
         for k, v in avg_score.items():
            p_avg_score=v
         p_avg_score=round(p_avg_score, 1)

         paginator=Paginator(reviews,5)
         page=request.GET.get('page')
         reviews=paginator.get_page(page)
         return render(request, 'detail.html',{'product_get':product_get, 'count':count, 'photo_get':photo_get, 'reviews':reviews, 'p_avg_score':p_avg_score})
      else:
         return render(request, 'detail.html',{'product_get':product_get, 'count':count, 'photo_get':photo_get})
'''

def search(request):
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}

   search_name=request.GET['search_name']
   min=request.GET['search_min']
   max=request.GET['search_max']
   search_cateogry=request.GET['search_cateogry']

   #???????????? ????????? ?????????
   if search_name:
      if min=="" and max=="" : # ??????????????? ??????
         products=product.objects.filter(name__contains=search_name)&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})

      elif min is not None and max=="": #?????????, ?????????
         products=product.objects.filter(name__contains=search_name)&product.objects.filter(price__range=(min, 1000000))&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})
      elif min=="" and max is not None: # ?????????, ?????????
         products=product.objects.filter(name__contains=search_name)&product.objects.filter(price__range=(0, max))&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})
      elif min is not None and max is not None: #?????????, ?????????, ?????????
         products=product.objects.filter(name__contains=search_name)&product.objects.filter(price__range=(min, max))&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})

    #????????? ???????????? ??????
   else:
      if min: #min ????????? ?????? ???
         if max=="": #min??? ????????? ??????
            products=product.objects.filter(price__range=(min, 1000000))&product.objects.all().filter(category=search_cateogry)
            return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})
         elif max: #min, max ????????? ??????
            products=product.objects.filter(price__range=(min, max))&product.objects.all().filter(category=search_cateogry)
            return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})

      elif max: #max??? ?????? ?????? ???
         products=product.objects.filter(price__range=(0, max))&product.objects.all().filter(category=search_cateogry)
         return render(request, 'search_rings.html', {'products':products, 'count':count, 'search_name':search_name, 'min':min, 'max':max, 'category':search_cateogry})
      else: #???????????? ?????? ???
         msg="???????????? ???????????? ???????????????."
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
    
     review_all=product.objects.all()
     review_set=review_all.filter(product_id=p_id)
     my_reviews=review.objects
     review_get=review.objects.filter(r_product__in=review_set)
     p_avg_score=review_get.aggregate(Avg('total_score'))
     
     paginator=Paginator(review_get,5)
     page=request.GET.get('page')
     r_posts=paginator.get_page(page)


     return render(request,"review_board.html", {'my_reviews':my_reviews,'r_posts':r_posts,'review_get':review_get,'p_avg_score':p_avg_score,'product_get':product_get,'count':count})

def review_view(request,product_id):
    product_get=product.objects.filter(product_id=product_id)
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    review_all=product.objects.all()
    review_set=review_all.filter(product_id=product_id)
    my_reviews=review.objects
    review_get=review.objects.filter(r_product__in=review_set)
    p_avg_score=review_get.aggregate(Avg('total_score'))
    
    
    paginator=Paginator(review_get,5)
    page=request.GET.get('page')
    r_posts=paginator.get_page(page)
   
    
   
    return render(request,"review_board.html", {'my_reviews':my_reviews,'r_posts':r_posts,'p_avg_score':p_avg_score,'product_get':product_get,'count':count,'review_get':review_get})

def address_after_detail(request):
   product_id=request.session.get('product_id')
   product_get=product.objects.filter(product_id=product_id)
   cart_count=context_processors.counter(request)
   cart_count=int(cart_count)
   count={'cart_count':cart_count}

   photo_all=product.objects.all()
   photo_set=photo_all.filter(product_id=product_id)
   photo_get=Photo.objects.filter(product__in=photo_set)
   
   user=request.session.get('user_id')
   account=UserAccounts.objects.get(user_id=user)
   address=Address.objects.get(accounts=account, is_default=True)

   product_set=product.objects.get(product_id=product_id)
   reviews=review.objects.filter(r_product=product_set)

   p_avg_score=reviews.aggregate(Avg('total_score'))

   return render(request, 'detail.html',{'product_get':product_get, 'count':count, 'photo_get':photo_get, 'address':address, 'reviews':reviews, 'p_avg_score':p_avg_score})
