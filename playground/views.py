from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product

# Create your views here.
def hello_world(request):
    
    product = Product.objects.get(pk=1)
    return render(request, 'hello.html', {"name": "Lucas", "age": 27})

