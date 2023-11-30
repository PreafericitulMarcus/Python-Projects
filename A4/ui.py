from vector_repository import VectorRepository
from tests import Test_UI


class UI:
    def __init__(self):
        self.non_stop = True
        self.vector_repo = VectorRepository()

    def menu(self):
        print(
            """
0. Exit 
1. Add vector to repository
2. Get all vectors
3. Get a vector at a given index 
4. Update a vector at a given index
5. Update a vector by "name_id"
6. Delete a vector by index
7. Delete a vector by "name_id"
8. Plot all vectors based on type and color
9. Get the list of vectors havgin a given sum
10. Delete all vectors between two indexes
11. Update all vectors having a given type by setting their color to the same given value
          """
        )

    def run(self):
        self.menu()
        self.vector_repo.vector_input()
        while self.non_stop:
            path = input("\nWhat path do you want to go: ")
            if Test_UI.test_path(path):
                path = int(path)
                if path == 0:
                    self.non_stop = False
                    print("exit...")

                elif path == 1:
                    try:
                        v_id = input("vector id: ")

                        v_type = int(input("type of vector: "))
                        if Test_UI.test_type(v_type) == False:
                            raise ValueError("type not found")

                        v_color = input("color of vector: ")
                        if Test_UI.test_color(v_color) == False:
                            raise ValueError("color not found")

                        v_values = input("vhat are the values of the vector: ")
                        values_list = []
                        for value in v_values.strip().split(" "):
                            values_list.append(int(value))
                        self.vector_repo.add_vector_to_repository(
                            v_id, v_color, v_type, values_list
                        )
                    except ValueError as err:
                        print("Error:", err)

                elif path == 2:
                    vectors = self.vector_repo.get_all_vectors()
                    for vector in vectors:
                        print(vector)

                elif path == 3:
                    try:
                        index = int(input("index of the vector: "))
                        print(self.vector_repo.get_vector_at_index(index))
                    except (IndexError, ValueError) as err:
                        print("Error:", err)

                elif path == 4:
                    try:
                        index = int(input("index of the vector to be updated: "))

                        new_color = input("new color: ")
                        if Test_UI.test_color(new_color) == False:
                            raise ValueError("color not found")

                        new_type = int(input("new type: "))
                        if Test_UI.test_type(new_type) == False:
                            raise ValueError("type not found")

                        new_values = input("new values (x y z..): ")

                        new_values_list = []
                        for value in new_values.split(" "):
                            new_values_list.append(int(value))

                        self.vector_repo.update_vector_at_index(
                            index, new_color, new_type, new_values_list
                        )
                    except (IndexError, ValueError) as err:
                        print("Error:", err)

                elif path == 5:
                    try:
                        search_name_id = input(
                            "what is the name_id of the vector to update?: "
                        )

                        new_color = input("new color: ")
                        if Test_UI.test_color(new_color) == False:
                            raise ValueError("color not found")

                        new_type = int(input("new type: "))
                        if Test_UI.test_type(new_type) == False:
                            raise ValueError("type not found")

                        new_values = input("new values (x y z..): ")

                        new_values_list = []
                        for value in new_values.split(" "):
                            new_values_list.append(int(value))

                        self.vector_repo.update_vector_at_name_id(
                            search_name_id, new_color, new_type, new_values_list
                        )
                    except (IndexError, ValueError) as err:
                        print("Error:", err)

                elif path == 6:
                    try:
                        index = int(input("index of the vector to be deleted: "))
                        self.vector_repo.delete_vector_by_index(index)
                    except (IndexError, ValueError) as err:
                        print("Error:", err)

                elif path == 7:
                    search_name_id = input("name_id of the vector to be deleted: ")
                    self.vector_repo.delete_vector_by_name_id(search_name_id)

                elif path == 8:
                    self.vector_repo.plot_vectors_in_chart()

                elif path == 9:
                    try:
                        sum_of_values = int(input("what is the sum of vecotrs?: "))
                        vectors_having_sum = self.vector_repo.get_vectors_having_sum(
                            sum_of_values
                        )
                        for vector in vectors_having_sum:
                            print(vector)
                    except ValueError as err:
                        print("Error:", err)

                elif path == 10:
                    try:
                        start_index = int(input("start index: "))
                        end_index = int(input("end index: "))
                        self.vector_repo.delete_vectors_between_indexes(
                            start_index, end_index
                        )
                    except (IndexError, ValueError) as err:
                        print("Error:", err)

                elif path == 11:
                    try:
                        vector_type = int(input("type of vector: "))
                        if Test_UI.test_type(vector_type) == False:
                            raise ValueError("type not found")

                        new_color = input("new color: ")
                        if Test_UI.test_color(new_color) == False:
                            raise ValueError("color not found")

                        self.vector_repo.update_vectors_by_type(vector_type, new_color)
                    except (ValueError, IndexError) as err:
                        print("Error:", err)


UI().run()
