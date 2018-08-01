from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import *
from .models import *


def index(request):
    return render(request, 'main/index.html')


def user(request):
    if request.user.is_authenticated:
        admin = Profile.objects.filter(user_type='salesadmin')
        manager = Profile.objects.filter(user_type='salesmanager')
        men = Profile.objects.filter(user_type='salesmen')
        context = {
            'admin': admin,
            'manager': manager,
            'men': men,
        }
        return render(request, 'main/user.html', context)
    else:
        return render(request, 'main/user.html')

def signup(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                f = form.save()
                f.refresh_from_db()  # load the profile instance created by the signal
                f.profile.user_type = form.cleaned_data.get('user_type')
                f.profile.sale_admin = str(form.cleaned_data.get('sale_admin'))
                f.profile.sale_manager = str(form.cleaned_data.get('sale_manager'))
                f.profile.first_name = form.cleaned_data.get('first_name')
                f.profile.last_name = form.cleaned_data.get('last_name')
                f.profile.mobile = form.cleaned_data.get('mobile')
                f.save()
                return redirect('main:user')
        else:
            form = SignUpForm()
        return render(request, 'main/signup.html', {'form': form})
    else:
        return render(request, 'main/not_authorised.html')


def login(request):
    if request.user.is_authenticated:
        return render(request, 'main/index.html')
    else:
        return render(request, 'login.html')


def auth_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect('main:index')
    else:
        return redirect('main:invalid')


def invalid(request):
    return render(request, 'main/invalid.html')


def logout(request):
    auth.logout(request)
    return redirect('main:login')


def customer(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.sale_manager = str(form.cleaned_data.get('sale_manager'))
                f.save()
                return redirect('main:customer_list')
        else:
            form = CustomerForm()
        return render(request, 'main/customer.html', {'form':form})
    else:
        return render(request, 'main/not_authorised.html')


def customer_list(request):
    sale_manager = Profile.objects.filter(user_type='salesmanager')
    customer = Customer.objects.all()
    context = {
        'sale_manager': sale_manager,
        'customer': customer,
    }
    return render(request, 'main/customer_list.html', context)