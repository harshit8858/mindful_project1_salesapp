from django.shortcuts import render, redirect
from.forms import *
from .models import *


def new_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order:new_order')
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
    return render(request, 'order/order_details.html', context)
