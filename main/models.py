from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


USER_TYPE = (
    ('salesadmin','SALES-ADMIN'),
    ('salesmanager','SALES-MANAGER'),
    ('salesmen','SALESMEN'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    sale_admin = models.CharField(max_length=20, null=True, blank=True)
    sale_manager = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Customer(models.Model):
    name = models.CharField(max_length=100)
    sale_manager = models.CharField(max_length=20)
    address = models.TextField(max_length=500)
    mobile = models.PositiveIntegerField()

    def __str__(self):
        return self.name
