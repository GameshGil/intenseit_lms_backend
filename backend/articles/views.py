from rest_framework import viewsets

from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """Представление для статей."""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
