from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


class News(models.Model):
    date = models.DateField(help_text='YYYY-MM-DD')
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("news:news_details", kwargs={"slug" : self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug
    qs = News.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_news_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_news_receiver, sender=News)
