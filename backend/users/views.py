from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer, UserFullInfoSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """Представление для пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_name='me', url_path='me')
    def get_current_user_info(self, request, pk=None):
        current_user = request.user
        return Response({'user': UserFullInfoSerializer(current_user).data})

    @action(detail=False, methods=['post'], url_name='reset_password',
            url_path='reset_password')
    def reset_user_password(self, request, pk=None):
        current_user = request.user
        return Response({'message': 'Временный пароль был выслан вам на почту '
                         f'{current_user.email}'})
