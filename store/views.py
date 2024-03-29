from django.shortcuts import get_object_or_404, render, Http404

from .models import Category, Product


def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, 'store/index.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True))
    return render(request, 'store/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = None
    try:
        product = get_object_or_404(Product, slug=slug, is_active=True)
    except Http404 as e:
        print(e)  # Вывести информацию об ошибке в консоль
    return render(request, 'store/single.html', {'product': product})
