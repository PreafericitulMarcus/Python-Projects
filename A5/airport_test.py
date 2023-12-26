import unittest
from airport_domain import Passengers, Plane
from airport_repository import AirportRepository


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
    def setUp(self):
        self.passanger = Passengers("John", "Doe", "123456789")
        self.passanger2 = Passengers("Will", "Smith", "987654321")
        self.passanger3 = Passengers("James", "Bond", "077777777")
        self.plane = Plane(1, "British Airways", 100, "London", [])

    def test_add_passenger(self):
        self.plane.add_passenger(self.passanger)
        self.assertEqual(self.plane.get_list_of_passengers(), [self.passanger])
        self.plane.add_passenger(self.passanger2)
        self.assertEqual(
            self.plane.get_list_of_passengers(), [self.passanger, self.passanger2]
        )
        self.plane.add_passenger(self.passanger3)
        self.assertEqual(
            self.plane.get_list_of_passengers(),
            [self.passanger, self.passanger2, self.passanger3],
        )

    def test_get_id(self):
        self.assertEqual(self.plane.get_id(), 1)

    def test_get_airline_company(self):
        self.assertEqual(self.plane.get_airline_company(), "British Airways")

    def test_get_numbe_of_seats(self):
        self.assertEqual(self.plane.get_number_of_seats(), 100)

    def test_get_destination(self):
        self.assertEqual(self.plane.get_destination(), "London")

    def test_get_list_of_passengers(self):
        self.assertEqual(self.plane.get_list_of_passengers(), [])

    def test_set_id(self):
        self.plane.set_id(2)
        self.assertEqual(self.plane.get_id(), 2)

    def test_set_airline_company(self):
        self.plane.set_airline_company("American Airlines")
        self.assertEqual(self.plane.get_airline_company(), "American Airlines")

    def test_set_number_of_seats(self):
        self.plane.set_number_of_seats(200)
        self.assertEqual(self.plane.get_number_of_seats(), 200)

    def test_set_destination(self):
        self.plane.set_destination("New York")
        self.assertEqual(self.plane.get_destination(), "New York")

    def test_set_list_of_passengers(self):
        self.plane.set_list_of_passengers([self.passanger, self.passanger2])
        self.assertEqual(
            self.plane.get_list_of_passengers(), [self.passanger, self.passanger2]
        )

    def test_delete_passenger(self):
        self.plane.set_list_of_passengers([self.passanger, self.passanger2])
        self.plane.delete_passenger(self.passanger)
        self.assertEqual(self.plane.get_list_of_passengers(), [self.passanger2])

    def test_delete_all_passengers(self):
        self.plane.set_list_of_passengers([self.passanger, self.passanger2])
        self.plane.delete_all_passengers()
        self.assertEqual(self.plane.get_list_of_passengers(), [])


class Test_AiportRepository(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
