from django.urls import reverse
from rest_framework import status
from django.utils import timezone

from .test_setup import CommonTestSetup
from articles.models import Article


class ArticleViewTestCase(CommonTestSetup):
    """Тестирование представления модели Article."""

    def test_get_article_list(self):
        response = self.client.get(reverse('articles:articles-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results')
        self.assertEqual(len(results), 1)
        check_data = {
            'title': 'Title of test article',
            'text': 'Text of test article',
            'author': 'test_user1',
            'area': 'Test area name'
        }
        for field, expected_value in check_data.items():
            self.assertEqual(results[0].get(field), expected_value)

    def test_get_article_detail(self):
        response = self.client.get(reverse(
            'articles:articles-detail',
            kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        check_data = {
            'title': 'Title of test article',
            'text': 'Text of test article',
            'author': 'test_user1',
            'area': 'Test area name'
        }
        for field, expected_value in check_data.items():
            self.assertEqual(response.data.get(field), expected_value)

    def test_create_article(self):
        data = {
            'title': 'Title of test article 2',
            'text': 'Text of test article 2',
            'author': self.user.id,
            'area': self.area.id,
            'pub_date': timezone.now()
        }
        response = self.client.post(
            reverse('articles:articles-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_object = Article.objects.latest('id')
        self.assertEqual(created_object.title, data['title'])
        self.assertEqual(created_object.text, data['text'])
        self.assertEqual(created_object.author.pk, data['author'])
        self.assertEqual(created_object.area.pk, data['area'])

    def test_update_article(self):
        data = {
            'title': 'Title of update article',
            'text': 'Text of update article',
            'author': self.user.id,
            'area': self.area.id,
            'pub_date': timezone.now()
        }
        response = self.client.put(reverse(
            'articles:articles-detail',
            kwargs={'pk': self.article.id}
            ), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        created_object = Article.objects.latest('id')
        self.assertEqual(created_object.title, data['title'])
        self.assertEqual(created_object.text, data['text'])
        self.assertEqual(created_object.author.pk, data['author'])
        self.assertEqual(created_object.area.pk, data['area'])

    def test_partial_update_article(self):
        data = {
            'title': 'Title of partial update article',
        }
        response = self.client.patch(reverse(
            'articles:articles-detail',
            kwargs={'pk': self.article.id}
            ), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        created_object = Article.objects.latest('id')
        self.assertEqual(created_object.title, data['title'])

    def test_delete_article(self):
        response = self.client.delete(reverse(
            'articles:articles-detail',
            kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Article.objects.count(), 0)

    def test_unauthorized_article_list(self):
        self.client.credentials()
        response = self.client.get(reverse('articles:articles-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_create_article(self):
        self.client.credentials()
        data = {
            'title': 'Title of test article 2',
            'text': 'Text of test article 2',
            'author': self.user.id,
            'area': self.area.id,
            'pub_date': timezone.now()
        }
        response = self.client.post(
            reverse('articles:articles-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Article.objects.count(), 1)

    def test_unauthorized_update_article(self):
        self.client.credentials()
        data = {
            'title': 'Unauthorized update of title',
            'text': 'Unauthorized update of text',
            'author': self.user.id,
            'area': self.area.id,
            'pub_date': timezone.now()
        }
        response = self.client.put(reverse(
            'articles:articles-detail',
            kwargs={'pk': self.article.id}
            ), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotEqual(self.article.title, data['title'])

    def test_unauthorized_delete_article(self):
        self.client.credentials()
        response = self.client.delete(reverse(
            'articles:articles-detail',
            kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Article.objects.count(), 1)

    def test_invalid_create_article(self):
        data = {
            'title': 'Invalid create of article',
            'author': self.user.id,
        }
        response = self.client.post(
            reverse('articles:articles-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Article.objects.count(), 1)

    def test_invalid_update_article(self):
        data = {
            'title': 'Invalid update of title',
            'author': self.user.id,
        }
        response = self.client.put(reverse(
            'articles:articles-detail',
            kwargs={'pk': self.article.id}
            ), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(self.article.title, data['title'])

    def test_invalid_delete_article(self):
        response = self.client.delete(
            reverse('articles:articles-detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Article.objects.count(), 1)

    def test_pagination_article_list_page_2(self):
        for i in range(22):
            Article.objects.create(
                title=f'Title of test article {i}',
                text=f'Text of test article {i}',
                author=self.user,
                area=self.area,
                pub_date=timezone.now()
            )
        response = self.client.get(
            reverse('articles:articles-list') + '?page=2')
        self.assertEqual(len(response.data.get('results')), 3)
