from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Area(models.Model):
    """Модель направлений курсов."""

    name = models.CharField(
        'Название направления',
        max_length=64,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self) -> str:
        return self.name[:50]


class Course(models.Model):
    """Модель курсов."""

    name = models.CharField(
        'Название курса',
        max_length=255,
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
        validators=[MinValueValidator(2023), MaxValueValidator(2040)],
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
        return self.name[:50]
