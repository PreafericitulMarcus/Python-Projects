from airport_domain import Passengers, Plane


class AirportRepository:
    """
    A class representing an airport repository.

    Attributes:
    - _passengers (list): A list of passengers.
    - _planes (list): A list of planes.

    Methods:
    - create_plane_from_file(): Creates planes from a file.
    - create_passenger_from_file(): Creates passengers from a file.
    - add_passenger(plane_id, first_name, last_name, passport_number): Adds a passenger to a plane.
    - add_plane(id, airline_company, numbers_of_seats, destination): Adds a plane to the repository.
    - get_all(): Returns all planes in the repository.
    - general_sort(list_to_sort, condition): Sorts a list based on a given condition.
    - delete_plane(plane_id): Deletes a plane from the repository.
    - delete_passenger(name): Deletes a passenger from the repository.
    - update_passenger(name, new_first_name, new_last_name): Updates the first name and last name of a passenger.
    - update_plane(old_plane_id, plane_id, new_airline_company, new_numbers_of_seats, new_destination): Updates the details of a plane.
    - sort_by_last_name(): Sorts the passengers in each plane by last name.
    - sort_by_number_of_seats(): Sorts the planes by number of seats.
    - sort_by_first_name_letter(substring): Sorts the planes by the count of passengers' first names starting with a given letter.
    - count_first_name_letter(plane, substring): Counts the number of passengers in a plane whose first name starts with a given letter.
    - sort_by_concatenation_passengers_destination(): Sorts the planes by concatenating the number of passengers and the destination.
    - concatenantion_passengers_destination(plane): Concatenates the number of passengers and the destination of a plane.
    - general_filter(list_to_filter, condition): Filters a list based on a given condition.
    - filter_by_same_first_three_numbers_of_passport_number(): Filters the planes based on whether they have passengers with the same first three numbers of their passport number.
    - same_prefix(plane): Checks if a plane has passengers with the same first three numbers of their passport number.
    - get_plane(plane_id): Returns a plane with a given ID.
    - filter_by_substring_in_first_last_name(plane_id, substring): Filters the passengers of a plane based on a substring in their first or last name.
    - filter_by_name(name): Filters the planes based on whether they have passengers with a given name.
    - same_name(plane, name): Checks if a plane has passengers with a given name.
    """

    def __init__(self):
        self._passengers = []
        self._planes = []

    #! CRUD operations
    def create_plane_from_file(self):
        with open("A5/plane_input.txt", "r") as f:
            for line in f.readlines():
                plane = line.split(" ")
                self.add_plane(plane[0], plane[1], plane[2], plane[3])

    def create_passenger_from_file(self):
        with open("A5/passangers_input.txt", "r") as f:
            for line in f.readlines():
                passenger = line.split(" ")
                self.add_passenger(
                    passenger[0], passenger[1], passenger[2], int(passenger[3])
                )

    def add_passenger(self, plane_id, first_name, last_name, passport_number):
        passenger = Passengers(first_name, last_name, passport_number)
        self._passengers.append(passenger)
        for plane in self._planes:
            if plane.get_id() == plane_id:
                plane.add_passenger(passenger)

    def add_plane(self, id, airline_company, numbers_of_seats, destination):
        plane = Plane(id, airline_company, numbers_of_seats, destination, [])
        self._planes.append(plane)

    def get_all(self):
        return self._planes

    def delete_plane(self, plane_id):
        for plane in self._planes:
            if plane.get_id() == plane_id:
                self._planes.remove(plane)

    def delete_passenger(self, name):
        for passenger in self._passengers:
            if passenger.get_first_name() + " " + passenger.get_last_name() == name:
                self._passengers.remove(passenger)
        for plane in self._planes:
            for passenger in plane.get_list_of_passengers():
                if passenger.get_first_name() + " " + passenger.get_last_name() == name:
                    plane.delete_passenger(passenger)

    def update_passenger(self, name, new_first_name, new_last_name):
        for passenger in self._passengers:
            if passenger.get_first_name() + " " + passenger.get_last_name() == name:
                passenger.set_first_name(new_first_name)
                passenger.set_last_name(new_last_name)
        for plane in self._planes:
            for passenger in plane.get_list_of_passengers():
                if passenger.get_first_name() + " " + passenger.get_last_name() == name:
                    passenger.set_first_name(new_first_name)
                    passenger.set_last_name(new_last_name)

    def update_plane(
        self,
        old_plane_id,
        plane_id,
        new_airline_company,
        new_numbers_of_seats,
        new_destination,
    ):
        for plane in self._planes:
            if plane.get_id() == old_plane_id:
                plane.set_id(plane_id)
                plane.set_airline_company(new_airline_company)
                plane.set_numbers_of_seats(new_numbers_of_seats)
                plane.set_destination(new_destination)

    #! Here is the sorting part
    def general_sort(self, list_to_sort, condition):
        for i in range(len(list_to_sort)):
            for j in range(i + 1, len(list_to_sort)):
                if not condition(list_to_sort[i], list_to_sort[j]):
                    list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]

    def sort_by_last_name(self):
        for plane in self._planes:
            self.general_sort(
                plane.get_list_of_passengers(),
                lambda x, y: x.get_last_name() < y.get_last_name(),
            )

    def sort_by_number_of_seats(self):
        self.general_sort(
            self._planes,
            lambda x, y: x.get_numbers_of_seats() < y.get_numbers_of_seats(),
        )

    def sort_by_first_name_letter(self, substring):
        self.general_sort(
            self._planes,
            lambda x, y: self.count_first_name_letter(x, substring)
            > self.count_first_name_letter(y, substring),
        )

    def count_first_name_letter(self, plane, substring):
        counter = 0
        for passenger in plane.get_list_of_passengers():
            if passenger.get_first_name()[0] == substring.upper():
                counter += 1
        return counter

    def sort_by_concatenation_passengers_destination(self):
        for plane in self._planes:
            self.general_sort(
                self._planes,
                lambda x, y: self.concatenantion_passengers_destination(x)
                < self.concatenantion_passengers_destination(y),
            )

    def concatenantion_passengers_destination(self, plane):
        return str(len(plane.get_list_of_passengers())) + str(plane.get_destination())

    #! Here is the filtering part
    def general_filter(self, list_to_filter, condition):
        filtered_list = []
        for element in list_to_filter:
            if condition(element):
                filtered_list.append(element)
        return filtered_list

    def filter_by_same_first_three_numbers_of_passport_number(self):
        return self.general_filter(self._planes, lambda plane: self.same_prefix(plane))

    def same_prefix(self, plane):
        passengers = plane.get_list_of_passengers()
        for i in range(len(passengers)):
            for j in range(i + 1, len(passengers)):
                prefix_i = str(passengers[i].get_passport_number())[:3]
                prefix_j = str(passengers[j].get_passport_number())[:3]
                if prefix_i == prefix_j:
                    return True
        return False

    def get_plane(self, plane_id):
        for plane in self._planes:
            if plane.get_id() == plane_id:
                return plane

    def filter_by_substring_in_first_last_name(self, plane_id, substring):
        plane = self.get_plane(plane_id)
        return self.general_filter(
            plane.get_list_of_passengers(),
            lambda passenger: substring in passenger.get_first_name()
            or substring in passenger.get_last_name(),
        )

    def filter_by_name(self, name):
        return (
            self.general_filter(self._planes, lambda plane: self.same_name(plane, name))
            if True
            else "Name not found"
        )

    def same_name(self, plane, name):
        passengers = plane.get_list_of_passengers()
        for passanger in passengers:
            if name == str(passanger.get_first_name()) + " " + str(
                passanger.get_last_name()
            ):
                return True
        return False
