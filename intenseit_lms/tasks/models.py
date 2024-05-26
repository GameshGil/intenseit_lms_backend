from django.db import models

from articles.models import Article


class Task(models.Model):
    """Модель заданий."""

    name = models.CharField(
        'Название задания',
        max_length=64,
        blank=False,
        null=False
    )
    text = models.TextField('Текст задания', blank=False, null=False)
    lesson = models.ForeignKey(
        Article,
        verbose_name='Статья занятия',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tasks'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self) -> str:
        return self.name[:50]
