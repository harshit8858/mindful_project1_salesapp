from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("msg:msg_details", kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(str(instance.user))

    if new_slug is not None:
        slug = new_slug
    qs = Message.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_message_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_message_receiver, sender=Message)
