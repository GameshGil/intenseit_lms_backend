from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для заданий."""

    def to_representation(self, instance):
        data = {
            'name': instance.name,
            'text': instance.text,
            'url': instance.get_absolute_url()
        }
        return data

    class Meta:
        model = Task
        fields = ('name', 'text', 'article')
