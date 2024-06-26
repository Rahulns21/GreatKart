from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products-by-category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='products-detail'),
    path('search/', views.search, name='search'),
]
