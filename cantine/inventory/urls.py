from django.urls import path
from django.contrib.auth.models import User
from inventory.views import Home, add_to_cart, remove_from_cart, decreaseCart, checkout, CartView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cart/<int:pk>/', add_to_cart, name='add-cart'),
    path('remove/<int:pk>/',remove_from_cart, name='remove-cart'),
    path('cart/', CartView,name='cart'),
    path('decrease/<int:pk>/', decreaseCart,name='decrease-cart'),
    path('cart/order_placed/', checkout, name='order_placed'),
    
] 