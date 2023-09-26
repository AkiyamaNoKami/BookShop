from django.shortcuts import get_object_or_404, render, Http404

from .models import Category, Product


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = None
    try:
        product = get_object_or_404(Product, slug=slug, in_stock=True)
    except Http404 as e:
        print(e)  # Вывести информацию об ошибке в консоль
    return render(request, 'store/products/single.html', {'product': product})
