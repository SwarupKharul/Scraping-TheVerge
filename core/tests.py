from django.test import TestCase
from .models import Article


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Article.objects.create(
            title="Big news",
            url="https://www.google.com",
            author="John Doe",
            date="2021-09-27 00:00:00",
        )

    def test_title_content(self):
        article = Article.objects.get(id=1)
        expected_object_name = f"{article.title}"
        self.assertEquals(expected_object_name, "Big news")

    def test_url_content(self):
        article = Article.objects.get(id=1)
        expected_object_name = f"{article.url}"
        self.assertEquals(expected_object_name, "https://www.google.com")

    def test_author_content(self):
        article = Article.objects.get(id=1)
        expected_object_name = f"{article.author}"
        self.assertEquals(expected_object_name, "John Doe")

    def test_date_content(self):
        article = Article.objects.get(id=1)
        expected_object_name = f"{article.date}"
        self.assertEquals(expected_object_name, "2021-09-27 00:00:00")
