from django.urls import path
from . import views

app_name = 'carts'
urlpatterns = [
    path('', views.cart, name='cart'),
    path('add-cart/<slug:product_slug>/', views.add_cart, name='add-cart'),
    path('remove-cart/<slug:product_slug>/<int:cart_item_id>/', views.remove_cart, name='remove-cart'),
    path('remove-cart-item/<slug:product_slug>/<int:cart_item_id>/', views.remove_cart_item, name='remove-cart-item'),
]
