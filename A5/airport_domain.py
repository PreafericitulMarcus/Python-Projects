class Passengers:
    """
    Represents a passenger in the airport.

    Attributes:
        __first_name (str): The first name of the passenger.
        __last_name (str): The last name of the passenger.
        __passport_number (int): The passport number of the passenger.
    """

    def __init__(self, first_name, last_name, passport_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__passport_number = passport_number

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_passport_number(self):
        return self.__passport_number

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_passport_number(self, passport_number):
        self.__passport_number = passport_number

    def __str__(self):
        return f"Passenger: {self.__first_name} {self.__last_name} with passport number {self.__passport_number}"


class Plane:
    """
    Represents a plane in an airport.

    Attributes:
        id (int): The unique identifier of the plane.
        airline_company (str): The name of the airline company.
        numbers_of_seats (int): The total number of seats in the plane.
        destination (str): The destination of the plane.
        list_of_passengers (list): The list of passengers in the plane.
    """

    def __init__(
        self, id, airline_company, numbers_of_seats, destination, list_of_passengers
    ):
        self.id = id
        self.airline_company = airline_company
        self.numbers_of_seats = numbers_of_seats
        self.destination = destination
        self.__list_of_passengers = list_of_passengers[:]

    def add_passenger(self, passenger):
        self.__list_of_passengers.append(passenger)

    def get_id(self):
        return self.id

    def get_airline_company(self):
        return self.airline_company

    def get_number_of_seats(self):
        return self.numbers_of_seats

    def get_destination(self):
        return self.destination

    def get_list_of_passengers(self):
        return self.__list_of_passengers

    def set_id(self, id):
        self.id = id

    def set_airline_company(self, airline_company):
        self.airline_company = airline_company

    def set_number_of_seats(self, numbers_of_seats):
        self.numbers_of_seats = numbers_of_seats

    def set_destination(self, destination):
        self.destination = destination

    def set_list_of_passengers(self, list_of_passengers):
        self.__list_of_passengers = list_of_passengers[:]

    def delete_passenger(self, passenger):
        self.__list_of_passengers.remove(passenger)

    def delete_all_passengers(self):
        self.__list_of_passengers.clear()

    def __str__(self):
        return f"Plane: {self.id}, company {self.airline_company}, with destination {self.destination} and {len(self.__list_of_passengers)} passengers out of {self.numbers_of_seats} and with passangers:\n{self.passangers_to_string()}"

    def passangers_to_string(self):
        string = ""
        for passenger in self.__list_of_passengers:
            string += str(passenger) + "\n"
        return string
