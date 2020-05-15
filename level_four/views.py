from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request,'level_four/index.html', context_dict)

def other(request):
    return render(request, 'level_four/other.html')

def relative(request):
    return render(request, 'level_four/rel_url_templates.html')