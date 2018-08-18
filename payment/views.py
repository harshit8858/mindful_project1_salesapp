from django.shortcuts import render, redirect
from .models import *
from .forms import *


def payment(request):
    payment = Payment.objects.all()
    context = {
        'payment': payment,
        'active7': 'active',
        'dropdown4': 'dropdown-container1',
    }
    return render(request, 'payment/payment.html', context)


def payment_add(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            f = form.save()
            f.save()
            return redirect('payment:payment_details', f.id)
    else:
        form = PaymentForm()
    context = {
        'form': form,
        'active7': 'active',
        'dropdown4': 'dropdown-container1',
    }
    if request.user.is_superuser:
        return render(request, 'payment/payment_add.html', context)
    else:
        return render(request, 'payment/not_authorized.html')


def payment_details(request, id):
    instance = Payment.objects.get(id=id)
    context = {
        'instance': instance,
        'active7': 'active',
        'dropdown4': 'dropdown-container1',
    }
    return render(request, 'payment/payment_details.html', context)


def payment_edit(request, id):
    instance = Payment.objects.get(id=id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=instance)
        if form.is_valid():
            f = form.save()
            f.save()
            return redirect('payment:payment_details', f.id)
    else:
        form = PaymentForm(instance=instance)
    context = {
        'form': form,
        'active7': 'active',
        'dropdown4': 'dropdown-container1',
    }
    if request.user.is_superuser:
        return render(request, 'payment/payment_add.html',context)
    else:
        return render(request, 'payment/not_authorized.html')


def payment_delete(request, id):
    instance = Payment.objects.get(id=id)
    instance.delete()
    return redirect('payment:payment')
