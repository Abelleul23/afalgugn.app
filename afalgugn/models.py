from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime

class LostItem(models.Model):
    item_name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='static/afalgugn/images')
    lost_date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=500)
    return_status = models.BooleanField(default=False)

    def was_lost_recently(self):
        return self.lost_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.item_name

@receiver(post_save, sender=LostItem)
def handle_lost_item_status(sender, instance, created, **kwargs):
    if instance.return_status:
        ReturnedItem.objects.create(
            item_name=instance.item_name,
            image=instance.image,
            location=instance.location,
            return_type='lost'
        )

class FoundItem(models.Model):
    item_name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='static/afalgugn/images')
    found_date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=500)
    return_status = models.BooleanField(default=False)

    def was_found_recently(self):
        return self.found_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.item_name

@receiver(post_save, sender=FoundItem)
def handle_found_item_status(sender, instance, created, **kwargs):
    if instance.return_status:
        ReturnedItem.objects.create(
            item_name=instance.item_name,
            image=instance.image,
            location=instance.location,
            return_type='found'
        )

class ReturnedItem(models.Model):
    RETURN_TYPES = [
        ('lost', 'Lost Item'),
        ('found', 'Found Item')
    ]

    item_name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='static/afalgugn/images')
    location = models.CharField(max_length=500)
    return_date = models.DateTimeField(auto_now_add=True)
    return_type = models.CharField(max_length=5, choices=RETURN_TYPES)

    def __str__(self):
        return self.item_name

    def was_returned_recently(self):
        return self.return_date >= timezone.now() - datetime.timedelta(days=1)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='static/afalgugn/profile_images', blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()