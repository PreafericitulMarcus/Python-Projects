class Passangers:
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
        return f"Passanger: {self.__first_name} {self.__last_name} with passport number {self.__passport_number}"

class Plane:
    def __init__(
        self, id, airline_company, numbers_of_seats, destination, list_of_passengers
    ):
        self.id = id
        self.airline_company = airline_company
        self.numbers_of_seats = numbers_of_seats
        self.destination = destination
        self.__list_of_passengers = list_of_passengers[:]  # maybe numpy?

    def get_id(self):
        return self.id

    def get_airline_company(self):
        return self.airline_company

    def get_numbers_of_seats(self):
        return self.numbers_of_seats

    def get_destination(self):
        return self.destination

    def get_list_of_passengers(self):
        return self.__list_of_passengers

    def set_id(self, id):
        self.id = id

    def set_airline_company(self, airline_company):
        self.airline_company = airline_company

    def set_numbers_of_seats(self, numbers_of_seats):
        self.numbers_of_seats = numbers_of_seats

    def set_destination(self, destination):
        self.destination = destination

    def set_list_of_passengers(self, list_of_passengers):
        self.__list_of_passengers = list_of_passengers[:]

    def __str__(self):
        return f"Plane: {self.id}, company {self.airline_company}, with destination {self.destination} and {len(self.__list_of_passengers)} passengers out of {self.numbers_of_seats}"