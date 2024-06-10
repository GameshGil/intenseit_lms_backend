from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet
from courses.views import CourseViewSet, LessonViewSet, get_analytics
from tasks.views import TaskViewSet
from users.views import UserViewSet

router = DefaultRouter()


router.register(r'users', UserViewSet, basename='users')
router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'courses', CourseViewSet, basename='courses')
router.register(
    r'courses/(?P<course_id>\d+)/lessons',
    LessonViewSet,
    basename='lessons'
)
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('analytics/', get_analytics, name='analytics')
]
