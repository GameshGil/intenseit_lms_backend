from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from courses.models import Course, Area

User = get_user_model()


class Article(models.Model):
    """Модель статей."""

    title = models.CharField(
        'Заголовок статьи',
        max_length=255,
        blank=False,
        null=False
    )
    text = models.TextField('Текст статьи', blank=False, null=False)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='articles',
        verbose_name='Автор статьи'
    )
    courses = models.ManyToManyField(
        Course,
        through='CourseArticle',
        null=True,
        blank=True,
        related_name='lessons',
    )
    area = models.ForeignKey(
        Area,
        verbose_name='Направление статьи',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='articles'
    )
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    update_date = models.DateTimeField('Дата изменения', auto_now=True)
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self) -> str:
        return self.title[:20]


class CourseArticle(models.Model):
    """Промежуточная модель занятий курсов."""

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )
    order_num = models.PositiveSmallIntegerField(
        'Порядковый номер занятия',
        blank=False,
        null=False
    )
