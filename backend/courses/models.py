from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


AREA_OBJECT_DESCR_MAX_LENGTH = 31
COURSE_OBJECT_DESCR_MAX_LENGTH = 31
AREA_NAME_MAX_LENGTH = 63
COURSE_NAME_MAX_LENGTH = 255
PROJECT_MIN_YEAR = 2022
PROJECT_MAX_YEAR = 2040


class Area(models.Model):
    """Модель направлений курсов."""

    name = models.CharField(
        'Название направления',
        max_length=AREA_NAME_MAX_LENGTH,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self) -> str:
        return self.name[:AREA_OBJECT_DESCR_MAX_LENGTH]


class Course(models.Model):
    """Модель курсов."""

    name = models.CharField(
        'Название курса',
        max_length=COURSE_NAME_MAX_LENGTH,
        blank=False,
        null=False
    )
    area = models.ForeignKey(
        Area,
        verbose_name='Направление курса',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='courses'
    )
    year = models.PositiveSmallIntegerField(
        'Год курса',
        validators=[
            MinValueValidator(PROJECT_MIN_YEAR),
            MaxValueValidator(PROJECT_MAX_YEAR)],
        blank=False,
        null=False
    )
    is_hidden = models.BooleanField(
        'Скрыт ли курс',
        default=False,
        blank=True,
        null=False
    )

    class Meta:
        ordering = ['-year', 'name']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self) -> str:
        return self.name[:COURSE_OBJECT_DESCR_MAX_LENGTH]
