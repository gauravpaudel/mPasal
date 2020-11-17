from django.contrib import admin
from django.urls import path
from apps.core.views import frontpage,contact,about
from apps.store.views import product_detail,category_detail
from apps.cart.views import cart_detail
from apps.store.api import api_add_to_cart,api_remove_from_cart, api_checkout
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('',frontpage,name='frontpage'),
	path('contact/',contact,name ='contact'),
    path('about/',about,name ='about'),
    path('cart/',cart_detail,name='cart_detail'),
    path('admin/', admin.site.urls),

    # API WHICH ARE USED IN VUE FRONTEND TO FETCH
    path('api/add_to_cart/',api_add_to_cart,name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    path('api/checkout/', api_checkout, name='api_checkout'),
    
    # Store 
	path('<slug:category_slug>/<slug:slug>/',product_detail,name='product_detail'),
    path('<slug:slug>/',category_detail,name='category_detail'),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)