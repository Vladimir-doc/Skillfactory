from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from .models import PostCategory, Post
from django.template.loader import render_to_string

from .tasks import send_notifications



@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        subscribers_emails = []

        for category in categories:
            subscribers = category.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]



        send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)