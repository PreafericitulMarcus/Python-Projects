from vector_logic import MyVector


class VectorRepository:
    def __init__(self):
        self.__data = []

    def vector_input(self):
        with open("vectors.txt", "r") as vectors:
            for vector in vectors:
                v_id, v_c, v_t, v_v = vector.strip().split(" ")
                self.add_vector_to_repository(v_id, v_c, v_t, v_v)

    def add_vector_to_repository(self, id, color, type, values):
        new_vector = MyVector(id, color, type, values)
        self.__data.append(new_vector)

    def get_all_vectors(self):
        return self.__data

    def get_vector_at_index(self, index):
        return self.__data[index]

    def update_vector_at_index(self, index, new_color, new_type, new_values):
        self.__data[index].set_color(new_color)
        self.__data[index].set_type(new_type)
        self.__data[index].set_values(new_values)
    