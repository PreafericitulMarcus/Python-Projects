from vector_repository import VectorRepository


class UI:
    def __init__(self):
        self.non_stop = True
        self.vector_repo = VectorRepository()

    def menu(self):
        print(
            """
1. Add vector to repository
2. Get all vectors
3. Get a vector at a given index 
4. Update a vector at a given index
5. Update a vector by "name_id"
6. Delete a vector by index
7. Delete a vector by "name_id"
8. Plot all vectors based on type and color
          """
        )

    def run(self):
        self.menu()
        self.vector_repo.vector_input()
        while self.non_stop:
            path = int(input("\nWhat path do you want to go: "))
            if path == 0:
                self.non_stop = False
                print("exit...")
            elif path == 1:
                pass
            elif path == 2:
                vectors = self.vector_repo.get_all_vectors()
                for vector in vectors:
                    print(vector)
            elif path == 3:
                index = int(input("index of the vector: "))
                print(self.vector_repo.get_vector_at_index(index))
            elif path == 4:
                index = int(input("index of the vector to be updated: "))
                new_color = input("new color: ")
                new_type = int(input("new type: "))
                new_values = input("new values (x y z..): ")

                new_values_list = []
                for value in new_values.split(" "):
                    new_values_list.append(int(value))
                self.vector_repo.update_vector_at_index(
                    index, new_color, new_type, new_values_list
                )


UI().run()