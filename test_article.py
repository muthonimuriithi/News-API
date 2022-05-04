import unittest
from app.models.news import Article


class TestArticle(unittest.TestCase):
    """Test Article"""

    def setUp(self):
        """Setup article test"""
        self.article = Article("Fed Meeting Latest News", 'Loise', '2022-05-04',
                               'Full coverage of the Federal Reserve May meeting', 'https://newsapi.org/', 'https://newsapi.org/')

    def test_instance(self):
        """Test that the Article class is well instanciated"""
        self.assertTrue(isinstance(self.article, Article))


if __name__ == '__main__':
    unittest.main()
