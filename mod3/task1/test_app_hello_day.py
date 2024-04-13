import unittest
from freezegun import freeze_time
from app import app


class TestHelloWorldWithDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_get_correct_username_with_weekday(self):
        username = 'username'
        response = self.app.get(self.base_url+username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time("2024-02-13")  # Вторник
    def test_get_username_with_correct_weekday(self):
        username = 'Хорошего понедельника'
        expected_response = f'Привет, {username}. Хорошего вторника!'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertEqual(response_text, expected_response)
