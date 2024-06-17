from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from articles.models import Article, CourseArticle
from courses.models import Course, Area


User = get_user_model()


class ArticleTestSetup(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test_user1',
            password='Abcqwert1',
            role='u'
        )
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.area = Area.objects.create(name='Test area name')
        self.course = Course.objects.create(
            name='Test course name',
            area=self.area,
            year=2024,
            is_hidden=False
        )
        self.article = Article.objects.create(
            title='Title of test article',
            text='Text of test article',
            author=self.user,
            area=self.area,
            pub_date=timezone.now()
        )
        self.article.courses.add(
            self.course, through_defaults={'order_num': 1})


class CourseArticleTestSetup(ArticleTestSetup):

    def setUp(self):
        super().setUp()
        self.course_article = CourseArticle.objects.get(pk=1)
