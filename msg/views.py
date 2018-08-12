from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from .forms import *
from .models import *


def msg(request):
    msg = Message.objects.all()
    context = {
        'msg': msg,
        'active3': 'active',
    }
    return render(request, 'msg/msg.html', context)


def msg_add(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            f = form.save()
            f.save()
            return HttpResponseRedirect(f.get_absolute_url())
    else:
        form = MessageForm()
    context = {
        'form': form,
        'active3': 'active',
    }
    if request.user.is_superuser:
        return render(request, 'msg/msg_add.html', context)
    else:
        return render(request, 'main/not_authorized.html')


def msg_details(request, slug):
    instance = get_object_or_404(Message, slug=slug)
    context = {
        'instance': instance,
        'active3': 'active',
    }
    return render(request, 'msg/msg_details.html', context)


def msg_edit(request, slug):
    instance = get_object_or_404(Message, slug=slug)
    if request.method == 'POST':
        form = MessageForm(request.POST,instance=instance)
        if form.is_valid():
            f = form.save()
            f.save()
            return HttpResponseRedirect(f.get_absolute_url())
    else:
        form = MessageForm(instance=instance)
    context = {
        'form': form,
        'active3': 'active',
    }
    if request.user.is_superuser:
        return render(request, 'msg/msg_add.html', context)
    else:
        return render(request, 'main/not_authorized.html')


def msg_delete(request, slug):
    instance = get_object_or_404(Message, slug=slug)
    if request.user.is_superuser:
        instance.delete()
    return redirect('msg:msg')
