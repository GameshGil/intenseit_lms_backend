from rest_framework import serializers

from .models import Article
from tasks.serializers import TaskSerializer


class ArticleSerializer(serializers.ModelSerializer):
    """Сериализатор для статей."""
    tasks = TaskSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['author'] is not None:
            data['author'] = instance.author.username
        if data['area'] is not None:
            data['area'] = instance.area.name
        return data

    class Meta:
        model = Article
        fields = ('title', 'text', 'author', 'area', 'tasks')
