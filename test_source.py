import unittest
from app.models.news import Source


class TestSource(unittest.TestCase):
    """Test Article"""

    def setUp(self):
        """Setup article test"""
        self.source = Source('bbc-news', 'BBC')

    def test_instance(self):
        """Test that the Source class is well instanciated"""
        self.assertTrue(isinstance(self.source, Source))


if __name__ == '__main__':
    unittest.main()
