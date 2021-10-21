from django.http import request
from django.shortcuts import get_object_or_404, render

from store.models import Product
from category.models import Category

def store(request, category_slug=None):
    products = None
    categories = None

    if category_slug != None:
        categories = get_object_or_404(Category,slug = category_slug)
        products = Product.objects.filter(category = categories, is_available = True)
    else:    
        products = Product.objects.all().filter(is_available = True)
        # product_count = products.count(), in the moment im geting the result in the html with products|lenght
    

    context = {
        'products':products,
        
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug , product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug=product_slug)
    except Exception as e:
        raise e  

    context = {
        'single_product':single_product
    }      
    return render(request, 'store/product_detail.html', context)
