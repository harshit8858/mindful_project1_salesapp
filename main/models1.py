from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Customer(models.Model):
    name = models.CharField(max_length=100)
    slug1 = models.SlugField(unique=True, blank=True, null=True)
    customer_code = models.CharField(max_length=100, blank=True, null=True)
    sale_manager = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    address = models.TextField(max_length=500)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    lattitude = models.PositiveIntegerField(blank=True, null=True)
    longitude = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url1(self):
        return reverse("main:customer_details", kwargs={"slug1" : self.slug1})

def create_slug(instance, new_slug=None):
    slug1 = slugify(instance.name)

    if new_slug is not None:
        slug1 = new_slug
    qs = Customer.objects.filter(slug1=slug1).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug1, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug1

def pre_save_customer_receiver(sender, instance, *args, **kwargs):
    if not instance.slug1:
        instance.slug1 = create_slug(instance)
pre_save.connect(pre_save_customer_receiver, sender=Customer)
