from django.urls import path
from .views import ProductListView, ShopView, HomeView, Savat, ProductUpdateView, CategoryView
urlpatterns = [
    path('detail/', ProductListView.as_view(), name='product-list'),
    path('shop/', ShopView.as_view(), name='product-shop'),
    path('savat/<int:id>', Savat.as_view(), name='product-savat'),
    path('category/<int:id>', CategoryView.as_view(), name='category'),
    path('pd/<int:id>', ProductUpdateView.as_view(), name='pd'),
]