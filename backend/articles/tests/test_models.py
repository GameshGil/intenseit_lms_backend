from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .test_setup import ArticleTestSetup, CourseArticleTestSetup
from articles.models import Article, CourseArticle

User = get_user_model()


class ArticleModelTest(ArticleTestSetup):
    """Тестирование для модели Article."""

    def test_article_creation(self):
        self.assertEqual(self.article.title, 'Title of test article')
        self.assertEqual(self.article.text, 'Text of test article')
        self.assertEqual(self.article.author.username, 'test_user1')
        self.assertEqual(self.article.courses.first().name, 'Test course name')

    def test_article_update(self):
        self.article.title = 'Update title of test article'
        self.article.save()
        self.assertEqual(self.article.title, 'Update title of test article')

    def test_article_delete(self):
        self.article.delete()
        self.assertEqual(Article.objects.count(), 0)

    def test_article_str(self):
        self.assertEqual(str(self.article), self.article.title[:20])

    def test_article_get_absolute_url(self):
        self.assertEqual(
            self.article.get_absolute_url(),
            f'/api/v1/articles/{self.article.pk}/'
        )

    def test_article_verbose_name(self):
        field_verbose_names = {
            'title': 'Заголовок статьи',
            'text': 'Текст статьи',
            'author': 'Автор статьи',
            'area': 'Направление статьи',
            'create_date': 'Дата создания',
            'update_date': 'Дата изменения',
            'pub_date': 'Дата публикации'
        }
        for field, expected_value in field_verbose_names.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.article._meta.get_field(field).verbose_name,
                    expected_value
                )

    def test_article_title_max_length(self):
        field_max_length = self.article._meta.get_field('title').max_length
        self.assertEqual(field_max_length, 255)

    def test_article_field_without_value(self):
        fields_with_null_allowed = {
            'title': False,
            'text': False,
            'author': True,
            'area': True,
            'create_date': False,
            'update_date': False,
            'pub_date': False
        }
        for field, expected_value in fields_with_null_allowed.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.article._meta.get_field(field).null,
                    expected_value
                )

    def test_article_author_relationship(self):
        self.assertEqual(self.article.author, self.user)

    def test_article_courses_relationship(self):
        self.assertEqual(self.article.courses.first(), self.course)

    def test_article_area_relationship(self):
        self.assertEqual(self.article.area, self.area)


class CourseArticleModelTest(CourseArticleTestSetup):
    """Тестирование для модели CourseArticle."""

    def test_course_article_creation(self):
        self.assertEqual(self.course_article.course.name, 'Test course name')
        self.assertEqual(
            self.course_article.article.title, 'Title of test article')
        self.assertEqual(self.course_article.order_num, 1)

    def test_course_article_update(self):
        self.course_article.order_num = 2
        self.course_article.save()
        self.assertEqual(self.course_article.order_num, 2)

    def test_course_article_delete(self):
        self.course_article.delete()
        self.assertEqual(CourseArticle.objects.count(), 0)

    def test_course_article_order_num_validator(self):
        obj_with_error = CourseArticle.objects.create(
            course=self.course,
            article=self.article,
            order_num=0
        )
        self.assertRaises(ValidationError, obj_with_error.full_clean)

    def test_course_article_get_absolute_url(self):
        self.assertEqual(
            self.course_article.get_absolute_url(),
            '/api/v1/courses/1/lessons/1/'
        )

    def test_course_article_verbose_name(self):
        field_verbose_names = {
            'course': 'Курс занятия',
            'article': 'Статья занятия',
            'order_num': 'Порядковый номер занятия'
        }
        for field, expected_value in field_verbose_names.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.course_article._meta.get_field(field).verbose_name,
                    expected_value
                )

    def test_course_article_course_relationship(self):
        self.assertEqual(self.course_article.course, self.course)

    def test_course_article_article_relationship(self):
        self.assertEqual(self.course_article.article, self.article)

    def test_course_article_order_num_without_value(self):
        self.assertEqual(
            self.course_article._meta.get_field('order_num').null,
            False
        )
