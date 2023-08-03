from django.shortcuts import render, redirect
from .models import *

def home(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'store.html', context)

def books(request):
    livros = Product.objects.filter(category__name="Livros")
    context = {'product':livros}
    return render(request, 'store.html', context)

def eletronics(request):
    eletronicos = Product.objects.filter(category__name="Eletrônicos")
    context = {'product':eletronicos}
    return render(request, 'store.html', context)

def productpage(request, id):
    item = Product.objects.filter(id=id)
    context = {'item':item}
    return render(request, 'productpage.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)

def payment(request):
    context = {}
    return render(request, 'payment.html', context)