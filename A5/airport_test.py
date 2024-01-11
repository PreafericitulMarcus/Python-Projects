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
    def setUp(self):
        self.airport_repo = AirportRepository()

    def test_create_plane_from_file(self):
        self.airport_repo.create_plane_from_file()
        planes = self.airport_repo.get_all()
        self.assertEqual(len(planes), 4)

    def test_create_passenger_from_file(self):
        self.airport_repo.create_passenger_from_file()
        passengers = self.airport_repo.get_all_passengers()
        self.assertEqual(len(passengers), 20)

    def test_add_passenger(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_passenger("P1", "John", "Doe", 123456789)
        passengers = self.airport_repo.get_all_passengers()
        self.assertEqual(len(passengers), 1)
        self.assertEqual(passengers[0].get_first_name(), "John")
        self.assertEqual(passengers[0].get_last_name(), "Doe")
        self.assertEqual(passengers[0].get_passport_number(), 123456789)

    def test_add_plane(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        planes = self.airport_repo.get_all()
        self.assertEqual(len(planes), 1)
        self.assertEqual(planes[0].get_id(), "P1")
        self.assertEqual(planes[0].get_airline_company(), "Airline A")
        self.assertEqual(planes[0].get_number_of_seats(), 100)
        self.assertEqual(planes[0].get_destination(), "Destination A")

    def test_get_all(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_plane("P2", "Airline B", 200, "Destination B")
        planes = self.airport_repo.get_all()
        self.assertEqual(len(planes), 2)

    def test_delete_plane(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.delete_plane("P1")
        planes = self.airport_repo.get_all()
        self.assertEqual(len(planes), 0)

    def test_delete_passenger(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_passenger("P1", "John", "Doe", 123456789)
        self.airport_repo.delete_passenger("John Doe")
        passengers = self.airport_repo.get_all_passengers()
        self.assertEqual(len(passengers), 0)

    def test_update_passenger(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_passenger("P1", "John", "Doe", 123456789)
        self.airport_repo.update_passenger(123456789, "Jane", "Smith", 987654321)
        passengers = self.airport_repo.get_all_passengers()
        self.assertEqual(len(passengers), 1)
        self.assertEqual(passengers[0].get_first_name(), "Jane")
        self.assertEqual(passengers[0].get_last_name(), "Smith")
        self.assertEqual(passengers[0].get_passport_number(), 987654321)

    def test_update_plane(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.update_plane("P1", "P2", "Airline B", 200, "Destination B")
        planes = self.airport_repo.get_all()
        self.assertEqual(len(planes), 1)
        self.assertEqual(planes[0].get_id(), "P2")
        self.assertEqual(planes[0].get_airline_company(), "Airline B")
        self.assertEqual(planes[0].get_number_of_seats(), 200)
        self.assertEqual(planes[0].get_destination(), "Destination B")

    def test_sort_by_last_name(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_passenger("P1", "John", "Doe", 123456789)
        self.airport_repo.add_passenger("P1", "Jane", "Smith", 987654321)
        self.airport_repo.sort_by_last_name()
        passengers = self.airport_repo.get_all_passengers()
        self.assertEqual(len(passengers), 2)
        self.assertEqual(passengers[0].get_last_name(), "Doe")
        self.assertEqual(passengers[1].get_last_name(), "Smith")

    def test_sort_by_number_of_seats(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_plane("P2", "Airline B", 200, "Destination B")
        self.airport_repo.sort_by_number_of_seats()
        planes = self.airport_repo.get_all()
        self.assertEqual(len(planes), 2)
        self.assertEqual(planes[0].get_number_of_seats(), 100)
        self.assertEqual(planes[1].get_number_of_seats(), 200)

    def test_sort_by_first_name_letter(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_passenger("P1", "John", "Doe", 123456789)
        self.airport_repo.add_passenger("P1", "Aane", "Smith", 987654321)
        self.airport_repo.sort_by_first_name_letter("J")
        planes = self.airport_repo.get_all()
        self.assertEqual(len(planes), 1)
        self.assertEqual(len(planes[0].get_list_of_passengers()), 2)
        self.assertEqual(planes[0].get_list_of_passengers()[0].get_first_name(), "John")
        self.assertEqual(planes[0].get_list_of_passengers()[1].get_first_name(), "Aane")

    def test_sort_by_concatenation_passengers_destination(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_plane("P2", "Airline B", 200, "Destination B")
        self.airport_repo.sort_by_concatenation_passengers_destination()
        planes = self.airport_repo.get_all()
        self.assertEqual(len(planes), 2)
        self.assertEqual(planes[0].get_destination(), "Destination A")
        self.assertEqual(planes[1].get_destination(), "Destination B")

    def test_filter_by_same_first_three_numbers_of_passport_number(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_passenger("P1", "John", "Doe", 123456789)
        self.airport_repo.add_passenger("P1", "Jane", "Smith", 987654321)
        filtered_planes = (
            self.airport_repo.filter_by_same_first_three_numbers_of_passport_number()
        )
        self.assertEqual(len(filtered_planes), 0)

    def test_filter_by_substring_in_first_last_name(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_passenger("P1", "John", "Doe", 123456789)
        self.airport_repo.add_passenger("P1", "Jane", "Smith", 987654321)
        filtered_passengers = self.airport_repo.filter_by_substring_in_first_last_name(
            "P1", "Jo"
        )
        self.assertEqual(len(filtered_passengers), 1)
        self.assertEqual(filtered_passengers[0].get_first_name(), "John")
        self.assertEqual(filtered_passengers[0].get_last_name(), "Doe")

    def test_filter_by_name(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_passenger("P1", "John", "Doe", 123456789)
        self.airport_repo.add_passenger("P1", "Jane", "Smith", 987654321)
        filtered_planes = self.airport_repo.filter_by_name("John Doe")
        self.assertEqual(len(filtered_planes), 1)
        self.assertEqual(filtered_planes[0].get_id(), "P1")

    def test_group_by_last_name(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_passenger("P1", "John", "Doe", 123456789)
        self.airport_repo.add_passenger("P1", "Jane", "Smith", 987654321)
        self.airport_repo.add_passenger("P1", "James", "Bond", 147852369)

        groups = list(self.airport_repo.group_by_last_name(1))
        # Verify the group for last name "Doe"
        doe_group = groups[0][0]

        self.assertEqual(doe_group.get_last_name(), "Doe")
        self.assertEqual(doe_group.get_first_name(), "John")

        # Verify the group for last name "Smith"
        smith_group = groups[1][0]
        self.assertEqual(smith_group.get_last_name(), "Smith")
        self.assertEqual(smith_group.get_first_name(), "Jane")

        # Verify the group for last name "Bond"
        bond_group = groups[2][0]
        self.assertEqual(bond_group.get_last_name(), "Bond")
        self.assertEqual(bond_group.get_first_name(), "James")

    def test_group_by_destination_different_company(self):
        self.airport_repo.add_plane("P1", "Airline A", 100, "Destination A")
        self.airport_repo.add_plane("P2", "Airline B", 200, "Destination A")
        self.airport_repo.add_plane("P3", "Airline C", 300, "Destination B")
        self.airport_repo.add_plane("P4", "Airline D", 400, "Destination B")

        groups = list(self.airport_repo.group_by_destination_different_company(1))

        # Verify the group for destination "Destination A"
        destination_a_group = groups[0][0]
        self.assertEqual(destination_a_group.get_destination(), "Destination A")
        self.assertEqual(destination_a_group.get_airline_company(), "Airline A")

        # Verify the group for destination "Destination B"
        destination_b_group = groups[1][0]
        self.assertEqual(destination_b_group.get_destination(), "Destination A")
        self.assertEqual(destination_b_group.get_airline_company(), "Airline B")


if __name__ == "__main__":
    unittest.main()
