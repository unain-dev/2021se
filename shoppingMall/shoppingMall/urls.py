"""shoppingMall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from shoppingApp import views as shoppingView
from productApp import views as productView
#from noticeApp import views as noticeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', shoppingView.logout_view, name="logout"),
    path('register/', shoppingView.register_view, name="join"),
    path('', shoppingView.login_view, name="userMain"),
    #category 경로-이후에 category table이 필요할까요..?
    
    path('category/bags', shoppingView.bags, name="bags"),
    path('category/hats', shoppingView.hats, name="hats"),
    path('category/necklace', shoppingView.necklace, name="necklace"),
    path('category/socks', shoppingView.socks, name="socks"),
    path('category/glasses', shoppingView.glasses, name="glasses"),
    
    path('products/', include('productApp.urls')),
    path('rings/', productView.rings, name="rings"),

    path('socks/', productView.socks, name="socks"),
    path('necklace/', productView.necklace, name="necklace"),
   
]
