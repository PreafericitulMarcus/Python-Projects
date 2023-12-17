from airport_repository import AirportRepository
from airport_test import Test_Ui
import sys

# from plane delete/update passenger
# can delete/update all


class Ui:
    def __init__(self):
        self.non_stop = True
        self.airport_repo = AirportRepository()
        self.airport_repo.create_plane_from_file()
        self.airport_repo.create_passenger_from_file()

    def menu(self):
        print(
            """

1. Sort the passengers in a plane by last name
2. Sort planes according to the number of passengers
3. Sort planes accordint to the number of passengers with the first name starting with a given substring
4. Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
5. Identify planes that have passengers with passport numbers starting with the same 3 letters
6. Identify passengers from a given plane for which the first name or last name contain a string given as parameter
7. Identify plane/s where there is a passenger with given name
8. Form groups of k passengers from the same plane but with different last names
9. Form groups of k planes with the same destination but belonging to different airline companies 
10. CRUD
    0. Missclick
    1. Add passenger
    2. Add plane
    3. Get all
    4. Update passenger
    5. Update plane
    6. Delete passenger
    7. Delete plane
0. Exit           

"""
        )

    def run(self):
        self.menu()
        while self.non_stop:
            try:
                path = int(input("\nEnter the path: "))
                if not 0 <= path <= 10:
                    raise IndexError("Index out of range")
            except (ValueError, IndexError) as e:
                print("Error!", e)
            else:
                if path == 0:
                    self.non_stop = False
                elif path == 1:
                    self.airport_repo.sort_by_last_name()
                    for plane in self.airport_repo.get_all():
                        print(plane)

                elif path == 2:
                    self.airport_repo.sort_by_number_of_seats()
                    for plane in self.airport_repo.get_all():
                        print(plane)

                elif path == 3:
                    try:
                        substring = input("Enter the substring: ")
                        if not substring.isalpha():
                            raise ValueError("Substring must be a string")
                        if len(substring) != 1:
                            raise ValueError("Substring must be a single character")
                    except ValueError as e:
                        print("Error!", e)
                    self.airport_repo.sort_by_first_name_letter(substring)
                    for plane in self.airport_repo.get_all():
                        print(plane)

                elif path == 4:
                    self.airport_repo.sort_by_concatenation_passengers_destination()
                    for plane in self.airport_repo.get_all():
                        print(plane)

                elif path == 5:
                    planes = (
                        self.airport_repo.filter_by_same_first_three_numbers_of_passport_number()
                    )
                    for plane in planes:
                        print(plane)

                elif path == 6:
                    try:
                        substring = input("Enter the substring: ")
                        plane_id = input("Enter the plane id: ")
                        if not substring.isalpha():
                            raise ValueError("Substring must be a string")
                    except ValueError as e:
                        print("Error!", e)
                    else:
                        passengers = (
                            self.airport_repo.filter_by_substring_in_first_last_name(
                                plane_id, substring
                            )
                        )
                        for passenger in passengers:
                            print(passenger)

                elif path == 7:
                    try:
                        name = input("Enter the name: ")
                        first_name = name.split()[0]
                        last_name = name.split()[1]
                        if not first_name.isalpha() or not last_name.isalpha():
                            raise ValueError("Name must be a string")
                    except ValueError as e:
                        print("Error!", e)
                    except IndexError:
                        print("Error!", "Name must have a first and last name")
                    else:
                        planes = self.airport_repo.filter_by_name(name)
                        for plane in planes:
                            print(plane)

                elif path == 10:
                    try:
                        sub_path = int(input("\nEnter the sub path: "))
                        if not 0 <= sub_path <= 7:
                            raise IndexError("Index out of range")
                    except (ValueError, IndexError) as e:
                        print("Error!", e)
                    else:
                        self.crud_operations(sub_path)

    def crud_operations(self, sub_path):
        if sub_path == 0:  # missclick
            pass
        elif sub_path == 1:  # add passanger
            plane_id = input("Enter the plane id: ")
            print("\nEnter the passenger data then type stop\n")
            writing = True
            while writing:
                try:
                    passanger = input("Enter the passenger data: ")
                    if passanger == "stop":
                        writing = False
                    else:
                        try:
                            passanger = passanger.split()
                            if len(passanger) != 3:
                                raise IndexError("Not enough data")
                            if not passanger[2].isdigit():
                                raise ValueError("Passport number must be a number")
                            first_name = passanger[0]
                            last_name = passanger[1]
                            passport_number = passanger[2]
                            self.airport_repo.add_passenger(
                                plane_id, first_name, last_name, passport_number
                            )
                        except (IndexError, ValueError) as e:
                            print("Error!", e)
                except ValueError as e:
                    print("Error!", e)
        elif sub_path == 2:  # add plane
            print("\nEnter plane data\n")
            try:
                id = input("Enter the id: ")
                airline_company = input("Enter the airline company: ")
                numbers_of_seats = int(input("Enter the number of seats: "))
                destination = input("Enter the destination: ")
                if not numbers_of_seats > 0:
                    raise ValueError("Number of seats must be a positive number")
                if not destination.isalpha():
                    raise ValueError("Destination must be a string")
                self.airport_repo.add_plane(
                    id,
                    airline_company,
                    numbers_of_seats,
                    destination,
                )
            except ValueError as e:
                print("Error!", e)
        elif sub_path == 3:  # get all
            for plane in self.airport_repo.get_all():
                print(plane)

        elif sub_path == 4:  # update passanger
            try:  # old passenger
                old_passenger = input("Enter the old passenger data: ")
                old_passenger = old_passenger.split()
                if len(old_passenger) != 3:
                    raise IndexError("Not enough data")
                if not old_passenger[2].isdigit():
                    raise ValueError("Passport number must be a number")
                first_name = old_passenger[0]
                last_name = old_passenger[1]
                passport_number = old_passenger[2]
            except (IndexError, ValueError) as e:
                print("Error!", e)
            else:
                try:  # new passenger
                    new_passenger = input("Enter the new passenger data: ")
                    new_passenger = new_passenger.split()
                    if len(new_passenger) != 3:
                        raise IndexError("Not enough data")
                    if not new_passenger[2].isdigit():
                        raise ValueError("Passport number must be a number")
                    first_name = new_passenger[0]
                    last_name = new_passenger[1]
                    passport_number = new_passenger[2]
                    self.airport_repo.update_passenger(
                        first_name, last_name, passport_number
                    )
                except (IndexError, ValueError) as e:
                    print("Error!", e)

        elif sub_path == 5:  # update plane
            try:
                old_plane_id = input("Enter the old plane id: ")
                new_plane = input("Enter the new plane data: ")
                new_plane = new_plane.split()
                if len(new_plane) != 4:
                    raise IndexError("Not enough data")
                if not new_plane[2].isdigit():
                    raise ValueError("Number of seats must be a number")
                if not new_plane[3].isalpha():
                    raise ValueError("Destination must be a string")
                id = new_plane[0]
                airline_company = new_plane[1]
                numbers_of_seats = new_plane[2]
                destination = new_plane[3]
                self.airport_repo.update_plane(
                    old_plane_id, id, airline_company, numbers_of_seats, destination
                )
            except (IndexError, ValueError) as e:
                print("Error!", e)
        elif sub_path == 6:  # delete passanger
            try:
                name = input("Enter the name: ")
                first_name = name.split()[0]
                last_name = name.split()[1]
                if not first_name.isalpha() or not last_name.isalpha():
                    raise ValueError("Name must be a string")
                self.airport_repo.delete_passenger(name)
            except ValueError as e:
                print("Error!", e)
            except IndexError:
                print("Error!", "Name must have a first and last name")

        elif sub_path == 7:  # delete plane
            try:
                id = input("Enter the id: ")
                self.airport_repo.delete_plane(id)
            except ValueError as e:
                print("Error!", e)


Ui().run()