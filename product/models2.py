from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


class PriceCategory(models.Model):
    price = models.CharField(max_length=100, unique=True)
    slug2 = models.SlugField(unique=True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.price

    def get_absolute_url2(self):
        return reverse("product:price_category_details", kwargs={"slug2" : self.slug2})

    class Meta:
        ordering = ["-timestamp" , "-last_updated"]

def create_slug(instance, new_slug=None):
    slug2 = slugify(instance.price)

    if new_slug is not None:
        slug2 = new_slug
    qs = PriceCategory.objects.filter(slug2=slug2).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug2, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug2

def pre_save_price_category_receiver(sender, instance, *args, **kwargs):
    if not instance.slug2:
        instance.slug2 = create_slug(instance)
pre_save.connect(pre_save_price_category_receiver, sender=PriceCategory)
