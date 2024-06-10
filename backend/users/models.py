from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.reverse import reverse


class CustomUser(AbstractUser):
    """Кастомная модель пользователя."""

    USER = 'u'
    ADMINISTRATOR = 'a'
    ROLE_CHOICES = [
        (USER, 'User'),
        (ADMINISTRATOR, 'Administrator')
    ]
    role = models.CharField(
        'Роль пользователя',
        max_length=1,
        choices=ROLE_CHOICES,
        default=USER
    )

    class Meta:
        ordering = ['pk']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username

    def get_absolute_url(self):
        return reverse('lms_api:users-detail', kwargs={'pk': self.pk})
