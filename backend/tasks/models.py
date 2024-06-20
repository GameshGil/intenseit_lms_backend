from django.db import models
from django.urls import reverse

from articles.models import Article


TASK_OBJECT_DESCR_MAX_LENGTH = 31
TASK_NAME_MAX_LENGTH = 255


class Task(models.Model):
    """Модель заданий."""

    name = models.CharField(
        'Название задания',
        max_length=TASK_NAME_MAX_LENGTH,
        blank=False,
        null=False
    )
    text = models.TextField('Текст задания', blank=False, null=False)
    article = models.ForeignKey(
        Article,
        verbose_name='Статья задания',
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
        return self.name[:TASK_OBJECT_DESCR_MAX_LENGTH]

    def get_absolute_url(self):
        return reverse('lms_api:tasks-detail', kwargs={'pk': self.pk})
