from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для курсов."""

    class Meta:
        model = Course
        fields = '__all__'
