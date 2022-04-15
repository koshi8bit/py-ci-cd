from unittest import TestCase
from src.main import index, api_v1_foo


class TestApp(TestCase):
    def test_app(self):
        self.assertEqual(api_v1_foo(), "bar")
