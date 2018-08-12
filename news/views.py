from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from .forms import *
from .models import *


def news(request):
    news = News.objects.all()
    context = {
        'news': news,
        'active3': 'active',
    }
    return render(request, 'news/news.html', context)


def news_add(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            f = form.save()
            f.save()
            return HttpResponseRedirect(f.get_absolute_url())
    else:
        form = NewsForm()
    context = {
        'form': form,
        'active2': 'active',
    }
    if request.user.is_superuser:
        return render(request, 'news/news_add.html', context)
    else:
        return render(request, 'main/not_authorized.html')


def news_details(request, slug):
    instance = get_object_or_404(News, slug=slug)
    context = {
        'instance': instance,
        'active2': 'active',
    }
    return render(request, 'news/news_details.html', context)


def news_edit(request, slug):
    instance = get_object_or_404(News, slug=slug)
    if request.method == 'POST':
        form = NewsForm(request.POST,instance=instance)
        if form.is_valid():
            f = form.save()
            f.save()
            return HttpResponseRedirect(f.get_absolute_url())
    else:
        form = NewsForm(instance=instance)
    context = {
        'form': form,
        'active2': 'active',
    }
    if request.user.is_superuser:
        return render(request, 'news/news_add.html', context)
    else:
        return render(request, 'main/not_authorized.html')


def news_delete(request, slug):
    instance = get_object_or_404(News, slug=slug)
    if request.user.is_superuser:
        instance.delete()
    return redirect('news:news')
