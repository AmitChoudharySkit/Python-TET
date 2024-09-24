from django.urls import path
from .views import get_products , create_product , product_detail
from api import views

urlpatterns = [
    path('products/' , get_products,name= 'get_product'),
    path('create' , create_product,name= 'create_product'),
    path('products/<int:pk>' , product_detail,name= 'product_detail'),
    path('' , views.index,name= 'home'),
    path('login' , views.loginUser,name= 'login'),
    path('logout/' , views.logoutUser,name= 'logout'),
]
