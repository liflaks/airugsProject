from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def catalog(request):
    return render(request, 'main/catalog.html')

def custom(request):
    return render(request, 'main/custom.html')

def cart(request):
    return render(request, 'main/cart.html')