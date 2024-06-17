from django.urls import reverse
from rest_framework import status
from .test_setup import ArticleTestSetup


class ArticleAPIsTest(ArticleTestSetup):
    """Тест доступности конечных точек статей."""

    def test_url_get_all_articles(self):
        response = self.client.get('/api/v1/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_all_articles_reverse(self):
        response = self.client.get(reverse('lms_api:articles-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_single_article(self):
        response = self.client.get('/api/v1/articles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_single_article_reverse(self):
        response = self.client.get(reverse(
            'lms_api:articles-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_all_users(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_all_users_reverse(self):
        response = self.client.get(reverse('lms_api:users-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_single_user(self):
        response = self.client.get('/api/v1/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_single_user_reverse(self):
        response = self.client.get(reverse(
            'lms_api:users-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_users_me(self):
        response = self.client.get('/api/v1/users/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_users_me_reverse(self):
        response = self.client.get(reverse('lms_api:users-me'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_post_users_reset_password(self):
        response = self.client.post('/api/v1/users/reset_password/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_post_users_reset_password_reverse(self):
        response = self.client.post(reverse('lms_api:users-reset_password'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_all_courses(self):
        response = self.client.get('/api/v1/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_all_courses_reverse(self):
        response = self.client.get(reverse('lms_api:courses-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_single_course(self):
        response = self.client.get('/api/v1/courses/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_single_course_reverse(self):
        response = self.client.get(reverse(
            'lms_api:courses-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_course_journal(self):
        response = self.client.get('/api/v1/courses/1/journal/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_course_journal_reverse(self):
        response = self.client.get(reverse(
            'lms_api:courses-journal', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_analytics(self):
        response = self.client.get('/api/v1/analytics/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_analytics_reverse(self):
        response = self.client.get(reverse('lms_api:analytics'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_all_lessons(self):
        response = self.client.get('/api/v1/courses/1/lessons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_all_lessons_reverse(self):
        response = self.client.get(reverse(
            'lms_api:lessons-list', kwargs={'course_id': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_single_lesson(self):
        response = self.client.get('/api/v1/courses/1/lessons/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_single_lesson_reverse(self):
        response = self.client.get(reverse(
            'lms_api:lessons-detail', kwargs={'pk': 1, 'course_id': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_all_tasks(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_all_tasks_reverse(self):
        response = self.client.get(reverse('lms_api:tasks-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_single_task(self):
        response = self.client.get('/api/v1/tasks/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url_get_single_task_reverse(self):
        response = self.client.get(reverse(
            'lms_api:tasks-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
