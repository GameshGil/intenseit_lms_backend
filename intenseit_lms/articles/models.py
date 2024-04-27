from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Article(models.Model):
    """Модель статей."""

    title = models.CharField('Заголовок статьи', max_length=255, blank=False)
    text = models.TextField('Текст статьи', blank=False)
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    update_date = models.DateTimeField('Дата изменения', auto_now=True)
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='articles',
        verbose_name='Автор публикации'
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self) -> str:
        return self.title[:20]
