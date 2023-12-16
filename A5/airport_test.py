import unittest
from airport_domain import Passengers, Plane


class Test_Passangers(unittest.TestCase):
    def setUp(self):
        self.passanger = Passengers("John", "Doe", "123456789")
        self.passanger2 = Passengers("Will", "Smith", "987654321")
        self.passanger3 = Passengers("James", "Bond", "077777777")

    def test_get_first_name(self):
        self.assertEqual(self.passanger.get_first_name(), "John")
        self.assertEqual(self.passanger2.get_first_name(), "Will")
        self.assertEqual(self.passanger3.get_first_name(), "James")

    def test_get_last_name(self):
        self.assertEqual(self.passanger.get_last_name(), "Doe")
        self.assertEqual(self.passanger2.get_last_name(), "Smith")
        self.assertEqual(self.passanger3.get_last_name(), "Bond")

    def test_get_passport_number(self):
        self.assertEqual(self.passanger.get_passport_number(), "123456789")
        self.assertEqual(self.passanger2.get_passport_number(), "987654321")
        self.assertEqual(self.passanger3.get_passport_number(), "077777777")

    def test_set_first_name(self):
        self.passanger.set_first_name("Jane")
        self.assertEqual(self.passanger.get_first_name(), "Jane")
        self.passanger2.set_first_name("Jada")
        self.assertEqual(self.passanger2.get_first_name(), "Jada")
        self.passanger3.set_first_name("Jenny")
        self.assertEqual(self.passanger3.get_first_name(), "Jenny")

    def test_set_last_name(self):
        self.passanger.set_last_name("Doe")
        self.assertEqual(self.passanger.get_last_name(), "Doe")
        self.passanger2.set_last_name("Austen")
        self.assertEqual(self.passanger2.get_last_name(), "Austen")
        self.passanger3.set_last_name("Jackson")
        self.assertEqual(self.passanger3.get_last_name(), "Jackson")

    def test_set_passport_number(self):
        self.passanger.set_passport_number("0000000000")
        self.assertEqual(self.passanger.get_passport_number(), "0000000000")
        self.passanger2.set_passport_number("11223344556")
        self.assertEqual(self.passanger2.get_passport_number(), "11223344556")
        self.passanger3.set_passport_number("789654123")
        self.assertEqual(self.passanger3.get_passport_number(), "789654123")


class Test_Plane(unittest.TestCase):
    pass


class Test_Ui:
    pass
