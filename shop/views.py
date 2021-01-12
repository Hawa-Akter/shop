from django.shortcuts import render, get_object_or_404
from.models import *

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    print(categories)
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)



    context = {'products': products,
               'category': category,
               'categories': categories

               }
    return render(request, 'shop/product/list.html', context)

def category_list(request):
    categories = Category.objects.all()

    context = {'categories': categories}
    return render(request, 'shop/product/category.html', context)