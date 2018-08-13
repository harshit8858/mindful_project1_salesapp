from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


USER_TYPE = (
    ('salesmanager','SALES-MANAGER'),
    ('salesmen','SALESMEN'),
)

STATUS = (
    ('active','ACTIVE'),
    ('inactive','INACTIVE'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE, null=True, blank=True, default='salesmanager')
    slug = models.SlugField(unique=True, blank=True, null=True)
    sale_manager = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS, default='active')
    address = models.CharField(max_length=1000, blank=True, null=True)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.FileField(upload_to='profile/profile_pic', blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("main:user_details", kwargs={"slug" : self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.user)

    if new_slug is not None:
        slug = new_slug
    qs = Profile.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_profile_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_profile_receiver, sender=Profile)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Company_Profile(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    pic = models.FileField(upload_to='comapany_profile', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.PositiveIntegerField(null=True, blank=True)
    fax = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    pan = models.CharField(max_length=100, null=True, blank=True)
    gst = models.CharField(max_length=100, null=True, blank=True)
    tan = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
