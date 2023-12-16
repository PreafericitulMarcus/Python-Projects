from airport_domain import Passengers, Plane


class AirportRepository:
    def __init__(self):
        self._passengers = []
        self._planes = []

    def create_plane_from_file(self):
        with open("A5/plane_input.txt", "r") as f:
            for line in f.readlines():
                plane = line.split(" ")
                self.add_plane(plane[0], plane[1], plane[2], plane[3])

    def create_passenger_from_file(self):
        with open("A5/passangers_input.txt", "r") as f:
            for line in f.readlines():
                passanger = line.split(" ")
                self.add_passenger(
                    passanger[0], passanger[1], passanger[2], int(passanger[3])
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

    def general_sort(self, condition):
        self._planes.sort(key=condition)

    def get_passangers(self):
        return self._passengers

    def sort_by_number_of_seats(self):
        self.general_sort(lambda plane: plane.get_numbers_of_seats())

    def sort_by_first_name_letter(self):
        self.general_sort(lambda plane: plane.get_first_name()[0])
