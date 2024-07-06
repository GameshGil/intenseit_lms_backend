from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.reverse import reverse

from courses.models import Course, Area


ARTICLE_NAME_MAX_LENGTH = 255
ARTICLE_OBJECT_DESCR_MAX_LENGTH = 20
ORDER_NUMBER_MIN_VALUE = 1


User = get_user_model()


class Article(models.Model):
    """Модель статей."""

    title = models.CharField(
        'Заголовок статьи',
        max_length=ARTICLE_NAME_MAX_LENGTH,
        blank=False,
        null=False,
        unique=True
    )
    text = models.TextField('Текст статьи', blank=False, null=False)
    author = models.ForeignKey(
        User,
        verbose_name='Автор статьи',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='articles'
    )
    courses = models.ManyToManyField(
        Course,
        through='CourseArticle',
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
        return self.title[:ARTICLE_OBJECT_DESCR_MAX_LENGTH]

    def get_absolute_url(self):
        return reverse('lms_api:articles-detail', kwargs={'pk': self.pk})


class CourseArticle(models.Model):
    """Промежуточная модель занятий курсов."""

    course = models.ForeignKey(
        Course,
        verbose_name='Курс занятия',
        on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        Article,
        verbose_name='Статья занятия',
        on_delete=models.CASCADE
    )
    order_num = models.PositiveSmallIntegerField(
        'Порядковый номер занятия',
        validators=[MinValueValidator(ORDER_NUMBER_MIN_VALUE)],
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['course', 'order_num']

    def get_absolute_url(self):
        return reverse(
            'lms_api:lessons-detail',
            kwargs={'pk': self.pk, 'course_id': self.course.id}
        )
