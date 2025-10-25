from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.http import HttpResponse
from store.models import Product
from store.models import Customer

# Create your views here.
def hello_world(request):
    
    customers = Customer.objects.all().order_by("-first_name")[:10]
    result = Product.objects.all().aggregate(count=Count(id), price=Max('price'))
    queryset = Product.objects.all().order_by('title')
    return render(request, 'hello.html', {"name": "Lucas", "age": 27, "products": list(queryset), "customers": list(customers), "result": result})

