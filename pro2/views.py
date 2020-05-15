from django.shortcuts import render, redirect
from pro2.models import User
from pro2.forms import SignInForm
# Create your views here.

def home(request):
    return render(request, 'pro2/homepage.html')

def redirect_home(request):
    return redirect('sign-in') #redirecting to url named as 'sign-in' in urls.py

def sign_in(request):
    return render(request, 'pro2/sign_in.html')

def sign_in_form(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESSFUL")
    
    return render(request, 'pro2/sign_in.html', {'form': form})

def add(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            new_user = User(fname = form.cleaned_data['fname'], lname = form.cleaned_data['lname'], email = form.cleaned_data['email'])
            new_user.save()
    return redirect('sign-in')

def index(request):
    data = User.objects.all()
    response = {'users':data}
    return render(request, 'pro2/index.html', context=response)