from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Webpage, AccessRecord, Topic

# Create your views here.

def index(request):
    return HttpResponse("<em>Hello World</em>")

def index2(request):
    my_dict = {'insert_me': "Hello!!! I am from views.py and you are in templates/firstapp"}
    return render(request, 'firstapp/index.html', context=my_dict)

def stat_load(request):
    return render(request, 'firstapp/loading_static.html')

def mod_index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_list}
    return render(request, 'firstapp/index_with_model.html', context=date_dict)