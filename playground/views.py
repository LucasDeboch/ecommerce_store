from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    x = 5
    y = 9
    return render(request, 'hello.html', {"name": "Lucas", "age": 27})
