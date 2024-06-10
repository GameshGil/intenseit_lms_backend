from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователей."""

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'get_absolute_url')


class UserFullInfoSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о пользователе."""

    class Meta:
        model = User
        exclude = ('password',)
