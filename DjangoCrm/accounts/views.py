from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def home(request):
    return render(request, 'accounts/dashboard.html')
def customer(request):
    return render(request, 'accounts/customer.html')
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products':products})
