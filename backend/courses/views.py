from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer, CourseListSerializer
from .serializers import LessonSerializer, LessonUpdateSerializer
from articles.models import CourseArticle


class CourseViewSet(viewsets.ModelViewSet):
    """Представление для курсов."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        return CourseSerializer

    @action(detail=True, methods=['get', 'patch'], url_name='journal',
            url_path='journal')
    def get_journal(self, request, pk=None):
        course = self.get_object()
        if request.method == 'PATCH':
            return Response(
                {'journal_data':
                 f'В журнал курса {course.name} внесены изменения.'})
        else:
            return Response({'journal_data': f'Журнал курса {course.name}.'})


@api_view()
def get_analytics(request):
    return Response({'info': 'Набор аналитических данных.'})


class LessonViewSet(viewsets.ModelViewSet):
    """Представления для занятий."""

    def get_course(self):
        return get_object_or_404(Course, pk=self.kwargs.get('course_id'))

    def get_queryset(self):
        return CourseArticle.objects.filter(course=self.get_course())

    def get_serializer_class(self):
        if self.action == 'update':
            return LessonUpdateSerializer
        return LessonSerializer
