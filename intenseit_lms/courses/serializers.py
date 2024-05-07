from django.db.models import Max
from rest_framework import serializers

from .models import Course
from articles.models import CourseArticle


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для занятий курса."""

    class Meta:
        model = CourseArticle
        fields = ('article',)

    def to_representation(self, instance):
        data = {
            'lesson_id': instance.id,
            'article_title': instance.article.title,
            'order_num': instance.order_num,
            'url': instance.get_absolute_url(),
            'article_url': instance.article.get_absolute_url()
        }
        return data

    def create(self, validated_data):
        view = self.context.get('view')
        max_order_num = view.get_queryset().aggregate(
            Max('order_num', default=0))
        lesson = CourseArticle.objects.create(
            course=view.get_course(),
            order_num=max_order_num['order_num__max'] + 1,
            **validated_data)
        return lesson


class LessonUpdateSerializer(LessonSerializer):
    """Сериализатор для изменения занятий курса."""

    class Meta:
        model = CourseArticle
        fields = ('order_num',)

    def update(self, instance, validated_data):
        view = self.context.get('view')
        current_order_num = instance.order_num
        new_order_num = validated_data.get('order_num', current_order_num)
        swap_lesson = view.get_queryset().filter(
            order_num=new_order_num).first()
        instance.order_num = new_order_num
        swap_lesson.order_num = current_order_num
        instance.save()
        swap_lesson.save()
        return instance


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для курсов."""

    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons(self, obj):
        lesson_list = CourseArticle.objects.filter(course=obj)
        return [LessonSerializer(lesson).data for lesson in lesson_list]


class CourseListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка курсов."""

    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, obj):
        return CourseArticle.objects.filter(course=obj).count()
