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

def telefonia(request):
    telefonia = Product.objects.filter(category__name="Telefonia")
    context = {'product':telefonia}
    return render(request, 'store.html', context)

def moveis(request):
    moveis = Product.objects.filter(category__name="Móveis")
    context = {'product':moveis}
    return render(request, 'store.html', context)

def eletrodomesticos(request):
    eletrodomesticos = Product.objects.filter(category__name="Eletrodomésticos")
    context = {'product':eletrodomesticos}
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