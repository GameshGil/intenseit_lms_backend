from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include((
        'articles.urls', 'articles'),
        namespace='lms_api'
    )),
    path(
        'api/v1/token/',
        TokenObtainPairView.as_view(),
        name='user_token_obtain'
    ),
    path(
        'api/v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='user_token_refresh'
    ),
]
