from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    slug1 = models.SlugField(unique=True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.category

    def get_absolute_url1(self):
        return reverse("product:category_details", kwargs={"slug1" : self.slug1})

    class Meta:
        ordering = ["-timestamp" , "-last_updated"]

def create_slug(instance, new_slug=None):
    slug1 = slugify(instance.category)

    if new_slug is not None:
        slug1 = new_slug
    qs = Category.objects.filter(slug1=slug1).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug1, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug1

def pre_save_category_receiver(sender, instance, *args, **kwargs):
    if not instance.slug1:
        instance.slug1 = create_slug(instance)
pre_save.connect(pre_save_category_receiver, sender=Category)
