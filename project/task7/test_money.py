import unittest

from app import app


class TestMoneyStorage(unittest.TestCase):
    def setUp(self):
        app.app.config['TESTING'] = True
        app.app.config['DEBUG'] = False
        app.storage = {2023: {8: 50, 9: 100, 12: 1000}}
        self.app = app.app.test_client()

    def test_adding_for_new_date(self):
        response = self.app.get('/add/20231223/1000')
        response_text = response.data.decode()
        self.assertEqual(app.storage[2023][12], 2000)

    def test_adding_for_exist_date(self):
        self.app.get('/add/20220923/1000')
        self.assertEqual(app.storage[2022][9], 1000)

    def test_uncorrected_date_format_catch_exception_message(self):
        with self.assertRaises(ValueError):
            self.app.get('/add/202480923/1000')

    def test_calculate_data_for_correct_year(self):
        response = self.app.get('/calculate/2023')
        response_text = response.data.decode()
        self.assertEqual(response_text, 'За период 2023 траты составили 1150')

    def test_calculate_data_for_correct_year_and_month(self):
        response = self.app.get('/calculate/2023/12')
        response_text = response.data.decode()
        self.assertEqual(response_text, 'За период 12/2023 траты составили 1000')

    def test_calculate_data_for_unexist_date(self):
        app.storage = {}
        response = self.app.get('/calculate/2023')
        response_text = response.data.decode()
        self.assertEqual(response_text, 'За период 2023 не было совершено трат')