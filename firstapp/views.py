from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Webpage, AccessRecord, Topic
from firstapp.forms import FormName

# Create your views here.

def index(request):
    #return HttpResponse("<em>Hello World</em>")
    return render(request, 'firstapp/index.html')

def index2(request):
    my_dict = {'insert_me': "Hello!!! I am from views.py and you are in templates/firstapp"}
    return render(request, 'firstapp/index.html', context=my_dict)

def stat_load(request):
    return render(request, 'firstapp/loading_static.html')

def mod_index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_list}
    return render(request, 'firstapp/index_with_model.html', context=date_dict)

def basic_form(request):
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESSFUL!")
            print("NAME: " +form.cleaned_data['name'])
            print("EMAIL: " +form.cleaned_data['email'])
            print("TEXT: " +form.cleaned_data['text'])

    return render(request, 'firstapp/form_basics.html', context={'form':form})