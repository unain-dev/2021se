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
from django.urls import path
from shoppingApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="join"),
    path('', views.login_view, name="userMain"),
    #category 경로-이후에 category table이 필요할까요..?
    path('category/rings', views.rings, name="rings"),
    path('category/bags', views.bags, name="bags"),
    path('category/hats', views.hats, name="hats"),
    path('category/necklace', views.necklace, name="necklace"),
    path('category/socks', views.socks, name="socks"),
    path('category/glasses', views.glasses, name="glasses"),
]
