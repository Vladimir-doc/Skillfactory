from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    about = models.CharField(max_length=128, null=True, blank=True, default='')
    avatar = models.ImageField(max_length=None, upload_to='avatars', null=True, blank=True)

    def __str__(self):
        if self.about:
            says = self.about[:20]
        else:
            says = 'Nothing yet'
        return f'{self.user} says {says}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.avatar.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
