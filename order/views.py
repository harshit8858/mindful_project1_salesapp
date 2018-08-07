from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from.forms import *
from .models import *


def new_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            f = form.save()
            f.save()
            return redirect('order:order_details', f.id )
            # return HttpResponseRedirect('')
    else:
        form = OrderForm()
    if request.user.is_superuser:
        return render(request, 'order/new_order.html', {'form':form})
    else:
        return render(request, 'main/not_authenticated.html')


def all_order(request):
    order = Order.objects.all()
    context = {
        'order': order,
    }
    return render(request, 'order/all_order.html', context)


def order_details(request, order_id):
    instance = Order.objects.get(id=order_id)
    context = {
        'instance': instance,
    }
    if request.user.is_superuser:
        return render(request, 'order/order_details.html', context)
    else:
        return render(request, 'main/not_authenticated.html')


def order_edit(request, order_id):
    instance = Order.objects.get(id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=instance)
        if form.is_valid():
            f = form.save()
            f.save()
            return redirect('order:order_details', f.id )
            # return HttpResponseRedirect('')
    else:
        form = OrderForm(instance=instance)
    if request.user.is_superuser:
        return render(request, 'order/new_order.html', {'form':form})
    else:
        return render(request, 'main/not_authenticated.html')


def order_delete(request, order_id):
    instance = Order.objects.get(id=order_id)
    instance.delete()
    return redirect('order:all_order')
