from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from .forms import *
from .models import *
from .models1 import *


def index(request):
    return render(request, 'main/index.html')


def user(request):
    if request.user.is_authenticated:
        # admin = Profile.objects.filter(user_type='salesadmin')
        manager = Profile.objects.filter(user_type='salesmanager')
        men = Profile.objects.filter(user_type='salesmen')
        context = {
            # 'admin': admin,
            'manager': manager,
            'men': men,
            'active10': 'active',
        }
        return render(request, 'main/user.html', context)
    else:
        return render(request, 'main/user.html')


def user_details(request, slug):
    instance = get_object_or_404(Profile, slug=slug)
    context = {
        'instance': instance,
        'active10': 'active',
    }
    return render(request, 'main/user_details.html', context)


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
                # return redirect('main:user')
                return HttpResponseRedirect(f.profile.get_absolute_url())
        else:
            form = SignUpForm()
        context = {
            'form': form,
            'active10': 'active',
        }
        return render(request, 'main/signup.html', context)
    else:
        return render(request, 'main/not_authorised.html')


def edit_user(request, slug):
    instance = get_object_or_404(Profile, slug=slug)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=instance)
            if form.is_valid():
                f = form.save()
                f.refresh_from_db()  # load the profile instance created by the signal
                f.user_type = form.cleaned_data.get('user_type')
                f.sale_admin = str(form.cleaned_data.get('sale_admin'))
                f.sale_manager = str(form.cleaned_data.get('sale_manager'))
                f.first_name = form.cleaned_data.get('first_name')
                f.last_name = form.cleaned_data.get('last_name')
                f.mobile = form.cleaned_data.get('mobile')
                f.save()
                # return redirect('main:user')
                return HttpResponseRedirect(f.get_absolute_url())
        else:
            form = EditUserForm(instance=instance)
        context = {
            'form': form,
            'active10': 'active',
        }
        return render(request, 'main/signup.html', context)
    else:
        return render(request, 'main/not_authorised.html')


def delete_user(request, slug):
    instance = get_object_or_404(Profile, slug=slug)
    instance.delete()
    return redirect('main:user')


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
                # return redirect('main:customer_list')
                return HttpResponseRedirect(f.get_absolute_url1())
        else:
            form = CustomerForm()
        context = {
            'form': form,
            'active5': 'active',
        }
        return render(request, 'main/customer.html', context)
    else:
        return render(request, 'main/not_authorised.html')


def customer_list(request):
    sale_manager = Profile.objects.filter(user_type='salesmanager')
    customer = Customer.objects.all()
    context = {
        'sale_manager': sale_manager,
        'customer': customer,
        'active5': 'active',
    }
    return render(request, 'main/customer_list.html', context)


def customer_details(request, slug1):
    instance = get_object_or_404(Customer, slug1=slug1)
    context = {
        'instance': instance,
        'active5': 'active',
    }
    return render(request, 'main/customer_details.html', context)


def edit_customer(request, slug1):
    instance = get_object_or_404(Customer, slug1=slug1)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CustomerForm(request.POST,instance=instance)
            if form.is_valid():
                f = form.save(commit=False)
                f.sale_manager = str(form.cleaned_data.get('sale_manager'))
                f.save()
                # return redirect('main:customer_list')
                return HttpResponseRedirect(f.get_absolute_url1())
        else:
            form = CustomerForm(instance=instance)
        context = {
            'form': form,
            'active5': 'active',
        }
        return render(request, 'main/customer.html', context)
    else:
        return render(request, 'main/not_authorised.html')


def delete_customer(request, slug1):
    instance = get_object_or_404(Customer, slug1=slug1)
    instance.delete()
    return redirect('main:customer_list')


def reports(request):
    context = {
        'active9': 'active',
    }
    return render(request, 'main/reports.html', context)


def dashboard(request):
    context = {
        'active1': 'active',
    }
    return render(request, 'main/dashboard.html', context)


def location_tracking(request):
    context = {
        'active8': 'active',
    }
    return render(request, 'main/location_tracking.html', context)


def payment(request):
    context = {
        'active7': 'active',
    }
    return render(request, 'main/payment.html', context)



def company_profile(request):
    cp = Company_Profile.objects.all()
    context = {
        'cp': cp,
        'active11': 'active',
    }
    if cp.count() == 0:
        if request.user.is_superuser:
            return redirect('main:company_profile_add')
        else:
            return render(request, 'main/no_data_found.html')
    else:
        return render(request, 'main/company_profile.html', context)


def company_profile_add(requset):
    if requset.method == 'POST':
        form = CompanyProfileEditForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('main:company_profile')
    else:
        form = CompanyProfileEditForm()
    context = {
        'form': form,
        'active11': 'active',
    }
    if requset.user.is_superuser:
        return render(requset, 'main/company_profile_add.html', context)
    else:
        return render(requset, 'main/not_authorised.html')


def company_profile_edit(requset, id):
    instance = Company_Profile.objects.get(id=id)
    if requset.method == 'POST':
        form = CompanyProfileEditForm(requset.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('main:company_profile')
    else:
        form = CompanyProfileEditForm(instance=instance)
    context = {
        'form': form,
        'instance': instance,
        'active11': 'active',
    }
    if requset.user.is_superuser:
        return render(requset, 'main/company_profile_add.html', context)
    else:
        return render(requset, 'main/not_authorised.html')