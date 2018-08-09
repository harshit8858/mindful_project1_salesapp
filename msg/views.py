from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from .forms import *
from .models import *


def messages(request):
    message = Message.objects.all()
    context = {
        'message': message,
    }
    return render(request, 'message/message.html', context)


def message_add(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            f = form.save()
            f.user = request.user
            f.save()
            return HttpResponseRedirect(f.get_absolute_url())
    else:
        form = MessageForm()
    context = {
        'form': form
    }
    if request.user.is_superuser:
        return render(request, 'message/messages_add.html', context)
    else:
        return render(request, 'main/not_authorized.html')


def message_details(request, slug):
    instance = get_object_or_404(Message, slug=slug)
    context = {
        'instance': instance,
    }
    return render(request, 'message/messages_details.html', context)


def message_edit(request, slug):
    instance = get_object_or_404(Message, slug=slug)
    if request.method == 'POST':
        form = MessageForm(request.POST,instance=instance)
        if form.is_valid():
            f = form.save()
            f.user = request.user
            f.save()
            return HttpResponseRedirect(f.get_absolute_url())
    else:
        form = MessageForm(instance=instance)
    context = {
        'form': form
    }
    if request.user.is_superuser:
        return render(request, 'message/messages_add.html', context)
    else:
        return render(request, 'main/not_authorized.html')


def message_delete(request, slug):
    instance = get_object_or_404(Message, slug=slug)
    if request.user.is_superuser:
        instance.delete()
    return redirect('message:message')
