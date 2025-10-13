
# Create your tests here.
from django.test import TestCase
from django.urls import reverse


class ArticlesTest(TestCase):
    def test_articles_list(self):
        response = self.client.get(reverse("article"))
        self.assertEqual(response.status_code, 200)

        # Проверяем наличие данных в контексте шаблона
        self.assertIn("article", response.context)
        articles = response.context["article"]

        # Проверяем не пустой ли список пользователей
        self.assertTrue(len(articles) > 0)
