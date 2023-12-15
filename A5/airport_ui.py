from airport_repository import AirportRepository
from airport_test import Test_Ui

# from plane delete/update passenger
# can delete/update all


class Ui:
    def __init__(self):
        self.non_stop = True
        self.airport_repo = AirportRepository()

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
0. Exit              
"""
        )

    def run(self):
        self.menu()
        while self.non_stop:
            try:
                path = int(input("Enter the path: "))
                if not 0 <= path <= 9:
                    raise IndexError("Index out of range")
            except (ValueError, IndexError) as e:
                print("Error!", e)
            else:
                if path == 0:
                    self.non_stop = False


Ui().run()
