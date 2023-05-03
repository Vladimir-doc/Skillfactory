from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Comments

@receiver(post_save, sender=Comments)
def notify_user_post(sender, instance, created, **kwargs):
    if created:
        post_author = instance.ad.author
        post_author.email_user(
            subject=f'Новый комментарий к вашему объявлению {instance.ad.title}',
            message=instance.text,
        )

    if instance.status:
        post_author = instance.ad.author
        post_author.email_user(
            subject=f'{instance.ad.author} принял ваш комментарий',
            message=f'Комментарий: {instance.text}',
        )

