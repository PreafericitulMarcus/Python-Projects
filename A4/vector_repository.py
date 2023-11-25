from vector_logic import MyVector
import matplotlib.pyplot as plt
import numpy as np


class VectorRepository:
    def __init__(self):
        self.__data = []

    def vector_input(self):
        with open("A4/vectors.txt", "r") as vectors:
            for vector in vectors:
                v_id, v_c, v_t, v_v_str = vector.strip().split(" ")
                v_v = []
                for val in v_v_str[1:-1].split(","):
                    v_v.append(int(val))
                self.add_vector_to_repository(int(v_id), str(v_c), int(v_t), v_v)

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

    def update_vector_at_name_id(self, search_name_id, new_color, new_type, new_values):
        for vector in self.__data:
            if vector.get_name_id() == search_name_id:
                vector.set_color(new_color)
                vector.set_type(new_type)
                vector.set_values(new_values)

    def delete_vector_by_index(self, index):
        self.__data.remove(self.__data[index])

    def delete_vector_by_name_id(self, search_name_id):
        for vector in self.__data:
            if vector.get_name_id() == search_name_id:
                self.__data.remove(vector)

    def plot_vectors_in_chart(self):
        for vector in self.__data:
            if vector.get_type() == 1:
                plt.plot(vector.get_values(), marker="o", color=vector.get_color())
            elif vector.get_type() == 2:
                plt.plot(vector.get_values(), marker="s", color=vector.get_color())
            elif vector.get_type() == 3:
                plt.plot(vector.get_values(), marker="v", color=vector.get_color())
            else:
                plt.plot(vector.get_values(), marker="D", color=vector.get_color())
        plt.show()
