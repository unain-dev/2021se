from django.urls import path
from productApp import views
from django.conf.urls.static import static
from django.conf import settings
app_name='products'
urlpatterns = [
    path('rings/',views.rings, name='rings'),
    path('glasses/',views.glasses, name='glasses'),
    path('necklace/',views.necklace, name='necklace'),
    path('hats/',views.hats, name='hats'),
    path('category/<str:category>',views.move_category, name='category'),
    path('detail/<int:product_id>',views.product_detail, name='detail'),
    path('search/', views.search, name="search"),
    #path('tempAdd/<int:product_id>', views.tempAdd, name="tempAdd"),
    #path('tempMinus/<int:product_id>', views.tempMinus, name="tempMinus"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
