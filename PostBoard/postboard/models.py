from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField



class Ad(models.Model):
    TYPE = (
        ('tanks', 'Танки'),
        ('heals', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildmasters', 'Гилдмастеры'),
        ('questgivers', 'Квестгиверы'),
        ('farriers', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potionmasters', 'Зельевары'),
        ('charmmasters', 'Мастер заклинаний'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    author_id = author.primary_key
    title = models.CharField(max_length=64, verbose_name='заголовок')
    text = RichTextField()
    category = models.CharField(max_length=64, choices=TYPE, default='tank', verbose_name='категория')
    time_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Объявление: {self.title}'

    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.pk)])

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comments(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объевление', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    time_in = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=64, verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Статус', default=False)

    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Пользователь {self.author} прокомментировал: {self.text}'




