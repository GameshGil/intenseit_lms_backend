from django.utils import timezone

from .test_setup import CommonTestSetup
from articles.serializers import ArticleSerializer
from tasks.serializers import TaskSerializer


class ArticleSerializerTestCase(CommonTestSetup):
    """Тестирование сериализации и десериализации модели Article."""

    def setUp(self) -> None:
        super().setUp()
        self.serializer = ArticleSerializer(instance=self.article)

    def test_article_contains_expected_fields(self):
        self.assertCountEqual(
            self.serializer.data.keys(),
            ['title', 'text', 'author', 'area', 'pub_date', 'tasks']
        )

    def test_article_fields_content(self):
        check_data = {
            'title': self.article.title,
            'text': self.article.text,
            'author': self.article.author.username,
            'area': self.article.area.name,
            'pub_date': self.article.pub_date.astimezone().isoformat(),
            'tasks': [TaskSerializer(self.task).data]
        }
        self.assertEqual(self.serializer.data, check_data)

    def test_article_valid_serialization(self):
        valid_data = {
            'title': 'Title of valid article',
            'text': 'Text of valid article',
            'author': self.user.id,
            'area': self.area.id,
            'pub_date': timezone.now()
        }
        serializer = ArticleSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    def test_article_invalid_serialization_missing_title_field(self):
        invalid_data = {
            'text': 'Text of invalid article',
            'author': self.user.id,
            'area': self.area.id,
            'pub_date': timezone.now()
        }
        serializer = ArticleSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    def test_article_invalid_serialization_missing_text_field(self):
        invalid_data = {
            'title': 'Title of invalid article',
            'author': self.user.id,
            'area': self.area.id,
            'pub_date': timezone.now()
        }
        serializer = ArticleSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('text', serializer.errors)

    def test_article_invalid_serialization_title_wrong_type(self):
        invalid_data = {
            'title': True,
            'text': 'Text of invalid article',
            'author': self.user.id,
            'area': self.area.id,
            'pub_date': timezone.now()
        }
        serializer = ArticleSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    def test_article_invalid_serialization_text_wrong_type(self):
        invalid_data = {
            'title': 'Title of invalid article',
            'text': True,
            'author': self.user.id,
            'area': self.area.id,
            'pub_date': timezone.now()
        }
        serializer = ArticleSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('text', serializer.errors)

    def test_article_invalid_serialization_author_wrong_type(self):
        invalid_data = {
            'title': 'Title of invalid article',
            'text': 'Text of invalid article',
            'author': 'Wrong type author',
            'area': self.area.id,
            'pub_date': timezone.now()
        }
        serializer = ArticleSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('author', serializer.errors)

    def test_article_invalid_serialization_area_wrong_type(self):
        invalid_data = {
            'title': 'Title of invalid article',
            'text': 'Text of invalid article',
            'author': self.user.id,
            'area': 'Wrong type area',
            'pub_date': timezone.now()
        }
        serializer = ArticleSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('area', serializer.errors)

    def test_article_invalid_serialization_pub_date_wrong_type(self):
        invalid_data = {
            'title': 'Title of invalid article',
            'text': 'Text of invalid article',
            'author': self.user.id,
            'area': self.area.id,
            'pub_date': 'Wrong type pub_date'
        }
        serializer = ArticleSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('pub_date', serializer.errors)

    def test_article_invalid_serialization_duplicate_title_field(self):
        invalid_data = {
            'title': 'Title of test article',
            'text': 'Text of article with duplicate title',
            'author': self.user.id,
            'area': self.area.id,
            'pub_date': timezone.now()
        }
        serializer = ArticleSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    def test_create_article(self):
        valid_data = {
            'title': 'Title of test article 2',
            'text': 'Text of test article 2',
            'author': self.user.id,
            'area': self.area.id
        }
        serializer = ArticleSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        test_article = serializer.save()
        self.assertEqual(test_article.title, 'Title of test article 2')
        self.assertEqual(test_article.text, 'Text of test article 2')
        self.assertEqual(test_article.author, self.user)
        self.assertEqual(test_article.area, self.area)

    def test_update_article(self):
        valid_data = {
            'title': 'Updated title of test article',
            'text': 'Updated text of test article',
            'author': self.user.id,
            'area': self.area.id
        }
        serializer = ArticleSerializer(instance=self.article, data=valid_data)
        self.assertTrue(serializer.is_valid())
        test_article = serializer.save()
        self.assertEqual(test_article.title, 'Updated title of test article')
        self.assertEqual(test_article.text, 'Updated text of test article')

    def test_partial_update_article(self):
        valid_data = {
            'title': 'Partially updated title of test article'
        }
        serializer = ArticleSerializer(
            instance=self.article, data=valid_data, partial=True)
        self.assertTrue(serializer.is_valid())
        test_article = serializer.save()
        self.assertEqual(
            test_article.title, 'Partially updated title of test article')
