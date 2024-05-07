from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()


router.register(r'courses', views.CourseViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
    path('analytics/', views.get_analytics, name='analytics')
]
