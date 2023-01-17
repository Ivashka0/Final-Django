from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from products.models import *


def start(request):
    return render(request, 'index.html')


def shop(request):
    context = Product.objects.all()
    categories = Category.objects.all()
    return render(template_name='shop.html', request=request, context={"products_list": context,
                                                                       "categories_list": categories})


def cart(request):
    context = Cart.objects.all()
    return render(template_name='busket.html', request=request, context={"busket_list": context})


# def add_cart(request, name):
#     prod = {}
#     products = Product.objects.values()
#     for element in range(len(products)):
#         if products[element]['name'] == name:
#             prod = products[element]
#         else:
#             continue
#     try:
#         _, created = Cart.objects.get_or_create(
#             name=prod['name'],
#             description=prod['description'],
#             price=prod['price'],
#             image_base64=prod['image_base64'],
#             available=prod['available']
#         )
#     except Exception as ex:
#         print(ex)
#         pass
#     context = Cart.objects.all()
#     return render(template_name='busket.html', request=request, context={"busket_list": context})


def add_cart(request, id1):
    product = Product.objects.filter(id=id1).values()
    try:
        _, created = Cart.objects.get_or_create(
            name=product[0]['name'],
            description=product[0]['description'],
            price=product[0]['price'],
            image_base64=product[0]['image_base64'],
            available=product[0]['available']
        )
    except Exception as ex:
        print(ex)
        pass
    context = Cart.objects.all()
    return render(template_name='busket.html', request=request, context={"busket_list": context})


def delete_cart(request, id1):
    Cart.objects.filter(id=id1).delete()
    context = Cart.objects.all()
    return render(template_name='busket.html', request=request, context={"busket_list": context})


def products_filter(request, category):
    context = Product.objects.filter(category__name=category)
    categories = Category.objects.all()

    return render(template_name='shop.html', request=request,
                  context={"products_list": context, "categories_list": categories})


def sort_cheapest(request):
    cheapest_products = Product.objects.all().order_by('price')

    return render(template_name='shop.html', request=request, context={"products_list": cheapest_products})


def sort_expensive(request):
    expensive_products = Product.objects.all().order_by('-price')

    return render(template_name='shop.html', request=request, context={"products_list": expensive_products})