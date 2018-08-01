from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    # image = models.ImageField(upload_to='product', null=True, blank=True)
    image = models.FileField(upload_to='product', null=True, blank=True)
    price = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product:product_details", kwargs={"slug" : self.slug})

    class Meta:
        ordering = ["-timestamp" , "-last_updated"]

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)

    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_product_receiver, sender=Product)

