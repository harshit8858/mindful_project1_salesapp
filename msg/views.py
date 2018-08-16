from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from main.models import *
from .forms import *
from .models import *


def msg(request):
    msg = Message.objects.all().order_by('-timestamp')
    profile = Profile.objects.all()
    for pro in profile:
        pro.msg_count = 0
        for m in msg:
            if m.user.username == pro.user.username:
                pro.msg_count = pro.msg_count + 1
                pro.save()
    context = {
        'msg': msg,
        'active3': 'active',
        'profile': profile,
    }
    return render(request, 'msg/msg.html', context)


def msg_user(request, d):
    instance = Profile.objects.get(id=d)
    msg = Message.objects.filter(user=instance.user).order_by('-timestamp')
    context = {
        'instance': instance,
        'msg': msg,
    }
    return render(request, 'msg/msg_user.html', context)


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
