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
#from noticeApp import views as noticeView
from django.conf import settings
from django.conf.urls.static import static
#from noticeApp import views as noticeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', shoppingView.logout_view, name="logout"),
    path('register/', shoppingView.register_view, name="join"),
    path('', shoppingView.login_view, name="userMain"),
    #category 경로-이후에 category table이 필요할까요..?
    
  
    path('create/', shoppingView.create_view, name='create'),
    path('postaddress/',shoppingView.postaddress, name='postaddress'),
    path('delete/<int:pk>/delete', shoppingView.delete, name='delete'),
    path('edit/<int:pk>', shoppingView.edit, name='edit'),
    path('editsave/', shoppingView.editsave, name='editsave'),
   
    path('newpost/', shoppingView.newpost, name='newpost'),
    path('products', include('productApp.urls', namespace='products')),
    #path('notice/', include('noticeApp.urls')),

    path('notice/', include('noticeApp.urls', namespace='notice')),
    path('cart/', include('cartApp.urls', namespace='cart')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

''' path('address/', shoppingView.address_view, name="address"),'''