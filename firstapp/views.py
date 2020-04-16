from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>Hello World</em>")

def index2(request):
    my_dict = {'insert_me': "Hello!!! I am from views.py and you are in templates/firstapp"}
    return render(request, 'firstapp/index.html', context=my_dict)

def stat_load(request):
    return render(request, 'firstapp/loading_static.html')