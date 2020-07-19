from django.contrib.auth.models import User, Group
from .models import Customer
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Customer')
        print(group)
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email

        )
        print('user profile created !!!')