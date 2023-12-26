from airport_domain import Passengers, Plane


class AirportRepository:
    def __init__(self):
        self._passengers = []  # list of Passengers
        self._planes = []  # list of Plane

    #! CRUD operations
    def create_plane_from_file(self):
        """Reads from file and creates a plane object"""
        with open("A5/plane_input.txt", "r") as f:
            for line in f.readlines():
                plane = line.split(" ")
                self.add_plane(plane[0], plane[1], plane[2], plane[3])

    def create_passenger_from_file(self):
        """Reads from file and creates a passenger object"""
        with open("A5/passangers_input.txt", "r") as f:
            for line in f.readlines():
                passenger = line.split(" ")
                self.add_passenger(
                    passenger[0], passenger[1], passenger[2], int(passenger[3])
                )

    def add_passenger(self, plane_id, first_name, last_name, passport_number):
        """
        Adds a passenger to the list of passengers and to the list of passengers of a plane
        plane_id: string, first_name: string, last_name: string, passport_number: int
        """
        passenger = Passengers(first_name, last_name, passport_number)
        self._passengers.append(passenger)
        for plane in self._planes:
            if plane.get_id() == plane_id:
                plane.add_passenger(passenger)

    def add_plane(self, id, airline_company, numbers_of_seats, destination):
        """
        Adds a plane to the list of planes
        id: string, airline_company: string, numbers_of_seats: int, destination: string
        """
        plane = Plane(id, airline_company, numbers_of_seats, destination, [])
        self._planes.append(plane)

    def get_all(self):
        """
        Return the list of planes which include the passengers
        """
        return self._planes

    def delete_plane(self, plane_id):
        """
        Deletes a plane from the list of planes
        plane_id: string
        """
        for plane in self._planes:
            if plane.get_id() == plane_id:
                self._planes.remove(plane)

    def delete_passenger(self, name):
        """
        Deletes a passenger from the list of passengers and from the list of passengers of a plane
        name: string
        """
        for passenger in self._passengers:
            if passenger.get_first_name() + " " + passenger.get_last_name() == name:
                self._passengers.remove(passenger)
        for plane in self._planes:
            for passenger in plane.get_list_of_passengers():
                if passenger.get_first_name() + " " + passenger.get_last_name() == name:
                    plane.delete_passenger(passenger)

    def update_passenger(
        self, old_passport_number, new_first_name, new_last_name, new_passport_number
    ):
        """
        Updates a passenger from the list of passengers and from the list of passengers of a plane by passport number
        old_passport_number: int, new_first_name: string, new_last_name: string, new_passport_number: int
        """
        for passenger in self._passengers:
            if passenger.get_passport_number() == old_passport_number:
                passenger.set_first_name(new_first_name)
                passenger.set_last_name(new_last_name)
                passenger.set_passport_number(new_passport_number)
        for plane in self._planes:
            for passenger in plane.get_list_of_passengers():
                if passenger.get_passport_number() == old_passport_number:
                    passenger.set_first_name(new_first_name)
                    passenger.set_last_name(new_last_name)
                    passenger.set_passport_number(new_passport_number)

    def update_plane(
        self,
        old_plane_id,
        plane_id,
        new_airline_company,
        new_numbers_of_seats,
        new_destination,
    ):
        """
        Updates a plane from the list of planes by plane id
        old_plane_id: string, plane_id: string, new_airline_company: string, new_numbers_of_seats: int, new_destination: string
        """
        for plane in self._planes:
            if plane.get_id() == old_plane_id:
                plane.set_id(plane_id)
                plane.set_airline_company(new_airline_company)
                plane.set_numbers_of_seats(new_numbers_of_seats)
                plane.set_destination(new_destination)

    #! Here is the sorting part
    def general_sort(self, list_to_sort, condition):
        """Sorts a list by a condition"""
        for i in range(len(list_to_sort)):
            for j in range(i + 1, len(list_to_sort)):
                if not condition(list_to_sort[i], list_to_sort[j]):
                    list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]

    def sort_by_last_name(self):
        """
        Sorts the list of passengers in a plane by last name
        """
        for plane in self._planes:
            self.general_sort(
                plane.get_list_of_passengers(),
                lambda x, y: x.get_last_name() < y.get_last_name(),
            )

    def sort_by_number_of_seats(self):
        """
        Sorts planes by the numbers of seats
        """
        self.general_sort(
            self._planes,
            lambda x, y: x.get_numbers_of_seats() < y.get_numbers_of_seats(),
        )

    def sort_by_first_name_letter(self, substring):
        """
        Sorts the list of passengers in a plane by the number of passengers whose first name starts with a given letter
        substring: string
        """
        self.general_sort(
            self._planes,
            lambda x, y: self.count_first_name_letter(x, substring)
            > self.count_first_name_letter(y, substring),
        )

    def count_first_name_letter(self, plane, substring):
        """
        Counts the number of passengers whose first name starts with a given letter
        plane: Plane, substring: string
        returns the counter
        """
        counter = 0
        for passenger in plane.get_list_of_passengers():
            if passenger.get_first_name()[0] == substring.upper():
                counter += 1
        return counter

    def sort_by_concatenation_passengers_destination(self):
        """
        Sorts the list of planes by the concatenation of the number of passengers and the destination
        """
        for plane in self._planes:
            self.general_sort(
                self._planes,
                lambda x, y: self.concatenantion_passengers_destination(x)
                < self.concatenantion_passengers_destination(y),
            )

    def concatenantion_passengers_destination(self, plane):
        """
        Concatenates the number of passengers and the destination
        plane: Plane
        returns the concatenation
        """
        return str(len(plane.get_list_of_passengers())) + str(plane.get_destination())

    #! Here is the filtering part
    def general_filter(self, list_to_filter, condition):
        """
        Filters a list by a condition
        returns the filtered list
        """
        filtered_list = []
        for element in list_to_filter:
            if condition(element):
                filtered_list.append(element)
        return filtered_list

    def filter_by_same_first_three_numbers_of_passport_number(self):
        """
        Filters the list of planes by the number of passengers whose first three numbers of passport number are the same
        """
        return self.general_filter(self._planes, lambda plane: self.same_prefix(plane))

    def same_prefix(self, plane):
        """
        Chaecks if the first three numbers of passport number are the same
        plane: Plane
        returns True if the first three numbers of passport number are the same, False otherwise
        """
        passengers = plane.get_list_of_passengers()
        for i in range(len(passengers)):
            for j in range(i + 1, len(passengers)):
                prefix_i = str(passengers[i].get_passport_number())[:3]
                prefix_j = str(passengers[j].get_passport_number())[:3]
                if prefix_i == prefix_j:
                    return True
        return False

    def get_plane(self, plane_id):
        """
        Gets a plane by plane id
        plane_id: string
        returns the plane
        """
        for plane in self._planes:
            if plane.get_id() == plane_id:
                return plane

    def filter_by_substring_in_first_last_name(self, plane_id, substring):
        """
        Filters the list of passengers in a plane by a substring in first name or last name
        plane_id: string, substring: string
        returns the filtered list
        """
        plane = self.get_plane(plane_id)
        return self.general_filter(
            plane.get_list_of_passengers(),
            lambda passenger: substring in passenger.get_first_name()
            or substring in passenger.get_last_name(),
        )

    def filter_by_name(self, name):
        """
        Filters the list of planes by a name
        name: string
        returns the filtered list
        """
        return (
            self.general_filter(self._planes, lambda plane: self.same_name(plane, name))
            if True
            else "Name not found"
        )

    def same_name(self, plane, name):
        """
        Checks if a name is in the list of passengers in a plane
        plane: Plane, name: string
        returns True if the name is in the list of passengers in a plane, False otherwise
        """
        passengers = plane.get_list_of_passengers()
        for passenger in passengers:
            if name == (passenger.get_first_name()) + " " + (passenger.get_last_name()):
                return True
        return False

    #! Here is the group part
    def is_valid(self, solution_list, condition):
        """
        Checks if a solution is valid
        solution_list: list, condition: function
        returns True if the solution is valid, False otherwise
        """
        for i in range(len(solution_list) - 1):
            if condition(solution_list[i], solution_list[i + 1]):
                return False
        return True

    def is_solution(self, solution_list, k):
        """
        Checks if a solution is a solution
        solution_list: list, k: int
        returns True if the solution is a solution, False otherwise
        """
        return k == len(solution_list)

    def backtracking(self, solution_list, k, domain, condition):
        """
        Backtracking algorithm
        solution_list: list, k: int, domain: list, condition: function
        returns the solution
        """
        if self.is_solution(solution_list, k):
            if self.is_valid(solution_list, condition):
                yield solution_list.copy()
        else:
            for i in range(len(domain)):
                element = domain[i]
                solution_list.append(element)
                yield from self.backtracking(
                    solution_list, k, domain[i + 1 :], condition
                )
                solution_list.pop()

    def group_by_last_name(self, k):
        """
        Forms a group of k passengers with the same last name
        k: int
        returns the solution
        """
        for plane in self._planes:
            domain = plane.get_list_of_passengers()
            solution_list = []
            condition = lambda x, y: x.get_last_name() == y.get_last_name()
            yield from self.backtracking(solution_list, k, domain, condition)

    def group_by_destination_different_company(self, k):
        """
        Forms a group of k planes with the same destination and different airline company
        k: int
        returns the solution
        """
        domain = self._planes
        solution_list = []
        condition = (
            lambda x, y: x.get_destination() == y.get_destination()
            and x.get_airline_company() == y.get_airline_company()
        )
        yield from self.backtracking(solution_list, k, domain, condition)
