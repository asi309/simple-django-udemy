from django.shortcuts import render
from pro2.models import User
# Create your views here.

def home(request):
    return render(request, 'pro2/homepage.html')

def index(request):
    data = User.objects.all()
    response = {'users':data}
    return render(request, 'pro2/index.html', context=response)