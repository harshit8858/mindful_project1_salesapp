from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


USER_TYPE = (
    ('salesadmin','SALES-ADMIN'),
    ('salesmanager','SALES-MANAGER'),
    ('salesmen','SALESMEN'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    sale_admin = models.CharField(max_length=20, null=True, blank=True)
    sale_manager = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.PositiveIntegerField(null=True, blank=True)

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
