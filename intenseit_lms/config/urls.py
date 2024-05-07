from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(('articles.urls', 'articles'),
                            namespace='articles')),
    path('api/v1/', include(('courses.urls', 'courses'), namespace='courses')),
    path('token/', TokenObtainPairView.as_view(), name='user_token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='user_token_refresh'),
]
