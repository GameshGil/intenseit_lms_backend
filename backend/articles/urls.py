from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

from .views import ArticleViewSet
from courses.views import CourseViewSet, LessonViewSet, get_analytics
from tasks.views import TaskViewSet
from users.views import UserViewSet

app_name = 'articles'

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
    path('analytics/', get_analytics, name='analytics'),
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='user_token_obtain'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='user_token_refresh'
    ),
]
