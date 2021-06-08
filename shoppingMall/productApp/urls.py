from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name='products'
urlpatterns = [
    path('category/<str:category>',views.move_category, name='category'),
    path('detail/<int:product_id>',views.product_detail, name='detail'),
   
    path('search/', views.search, name="search"),
    path('review_post/<int:pk>', views.review_post, name="review_post"),
    path('review_save/', views.review_save, name="review_save"),
    path('review_board/<int:product_id>', views.review_view, name="review_board"),
    path('detail/', views.address_after_detail, name="address_after_detail")
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



