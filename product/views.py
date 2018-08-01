from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from .models1 import *


def category(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'product/category.html', context)


def product(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'product/product.html', context)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.created_by = request.user
            f.save()
            return redirect(f.get_absolute_url1())
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    if request.user.is_superuser:
        return render(request, 'product/add_category.html', context)
    else:
        return render(request, 'main/not_authorised.html')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.created_by = request.user
            f.save()
            # return redirect('product:index')
            return HttpResponseRedirect(f.get_absolute_url())
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    if request.user.is_superuser:
        return render(request, 'product/add_product.html', context)
    else:
        return render(request, 'main/not_authorised.html')


def product_detail(request, slug):
    instance = get_object_or_404(Product, slug=slug)
    context = {
        'instance': instance
    }
    return render(request, 'product/product_details.html', context)


def product_edit(request, slug):
    instance = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            f = form.save(commit=False)
            f.created_by = request.user
            f.save()
            # return redirect('product:index')
            return HttpResponseRedirect(f.get_absolute_url())
    else:
        form = ProductForm(instance=instance)
    context = {
        'form': form,
    }
    if request.user.is_superuser:
        return render(request, 'product/product.html', context)
    else:
        return render(request, 'main/not_authorised.html')


def category_detail(request, slug1):
    instance = get_object_or_404(Category, slug1=slug1)
    product =  Product.objects.all()
    context = {
        'instance': instance,
        'product': product
    }
    return render(request, 'product/category_details.html', context)


def category_edit(request, slug1):
    instance = get_object_or_404(Category, slug1=slug1)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            f = form.save(commit=False)
            f.created_by = request.user
            f.save()
            # return redirect('product:index')
            return HttpResponseRedirect(f.get_absolute_url1())
    else:
        form = CategoryForm(instance=instance)
    context = {
        'form': form,
    }
    if request.user.is_superuser:
        return render(request, 'product/category.html', context)
    else:
        return render(request, 'main/not_authorised.html')
