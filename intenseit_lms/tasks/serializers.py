from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для заданий."""

    class Meta:
        model = Task
        fields = ('name', 'text', 'lesson')
