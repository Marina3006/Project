import unittest

from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Al', 1999, 'Moscow')

    def test_return_correct_age(self):
        self.assertEqual(self.person.get_age(), 25)

    def test_get_correct_name(self):
        self.assertEqual(self.person.get_name(), 'Al')

    def test_possible_to_change_the_name(self):
        self.person.set_name('Alexandr')
        self.assertEqual(self.person.name, 'Alexandr')

    def test_get_correct_address(self):
        self.assertEqual(self.person.get_address(), 'Moscow')

    def test_possible_to_change_the_address(self):
        self.person.set_address('Yekaterinburg')
        self.assertEqual(self.person.address, 'Yekaterinburg')

    def test_check_existing_address_must_return_false(self):
        self.assertEqual(self.person.is_homeless(), False)

    def test_check_not_existing_address_must_return_true(self):
        self.person.address = None
        self.assertEqual(self.person.is_homeless(), True)