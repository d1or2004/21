from django.shortcuts import render
from .models import ShopDetails, Product
from django.views import View


class ProductListView(View):
    def get(self, request):
        product = Product.objects.all()
        context = {'product': product}
        return render(request, 'main/shop-detail.html', context)


class ShopView(View):
    def get(self, request):
        shop = ShopDetails.objects.all()
        context = {'shop': shop}
        return render(request, 'main/shop.html', context)


class HomeView(View):
    def get(self, request):
        home = Product.objects.all()
        context = {'home': home}
        return render(request, 'main/index.html', context)


class Savat(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        context = {'product': product}
        return render(request, 'main/savat.html', context)


class CategoryView(View):
    def get(self, request):
        search = Product.objects.get('search')
        if not search:
            category = Product.objects.all()
            context = {'category': category}
            return render(request, 'main/index.html', context)
        else:
            category = Product.objects.filter(name__icontains=search)
            if category:
                context = {'category': category}
                return render(request, 'main/index.html', context)
            else:
                context = {'category': category}
                return render(request, 'main/index.html', context)


class ProductUpdateView(View):
    def get(self, request, id):
        products = Product.objects.filter(category_id=id)
        context = {'products': products}
        return render(request, 'main/index.html', context)
