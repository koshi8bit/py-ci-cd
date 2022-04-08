from unittest import TestCase
from src.main import index


class TestApp(TestCase):
    def test_app(self):
        self.assertEqual(index(), "Hello world")
