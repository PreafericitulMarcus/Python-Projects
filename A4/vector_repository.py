from vector_logic import MyVector
import matplotlib.pyplot as plt


class VectorRepository:
    def __init__(self):
        self.__data = []

    def vector_input(self):
        '''
        Function gets values from a file and puts them in data list
        '''
        with open("A4/vectors.txt", "r") as vectors:
            for vector in vectors:
                v_name_id, v_c, v_t, v_v_str = vector.strip().split(" ")
                v_v = []
                for val in v_v_str[1:-1].split(","):
                    v_v.append(int(val))
                self.add_vector_to_repository(v_name_id, str(v_c), int(v_t), v_v)

    def add_vector_to_repository(self, name_id, color, type, values):
        '''
        Function adds a new vector to the data list
        name_id - string, color - string, type - integer, values - list of integers
        '''
        new_vector = MyVector(name_id, color, type, values)
        self.__data.append(new_vector)

    def get_all_vectors(self):
        '''
        Function returns the data list
        '''
        return self.__data

    def get_vector_at_index(self, index):
        '''
        Function returns the vector at the given index
        '''
        return self.__data[index]

    def update_vector_at_index(self, index, new_color, new_type, new_values):
        '''
        Function updates the vector at the given index
        index - integer, new_color - string, new_type - integer, new_values - list of integers
        '''
        self.__data[index].set_color(new_color)
        self.__data[index].set_type(new_type)
        self.__data[index].set_values(new_values)

    def update_vector_at_name_id(self, search_name_id, new_color, new_type, new_values):
        '''
        Function updates the vector with the given name_id
        search_name_id - string, new_color - string, new_type - integer, new_values - list of integers
        '''
        for vector in self.__data:
            if vector.get_name_id() == search_name_id:
                vector.set_color(new_color)
                vector.set_type(new_type)
                vector.set_values(new_values)

    def delete_vector_by_index(self, index):
        '''
        Function deletes the vector at the given index
        index - integer
        '''
        self.__data.remove(self.__data[index])

    def delete_vector_by_name_id(self, search_name_id):
        '''
        Function deletes the vector with the given name_id
        search_name_id - integer
        '''
        for vector in self.__data:
            if vector.get_name_id() == search_name_id:
                self.__data.remove(vector)

    def plot_vectors_in_chart(self):
        '''
        Function plots the vectors in a chart
        '''
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

    def get_vectors_having_sum(self, sum_of_values):
        '''
        Function returns a list of vectors having the sum of their values equal to a given sum
        sum_of_values - integer
        '''
        vectors_having_sum = []
        for vector in self.__data:
            summ = 0
            summ += vector.sum_elem_vector()
            if summ == sum_of_values:
                vectors_having_sum.append(vector)
        return vectors_having_sum

    def delete_vectors_between_indexes(self, index1, index2):
        '''
        Function deletes the vectors between two given indexes
        index1, index2 - integers
        '''
        if index1 > index2:
            index1, index2 = index2, index1
        for i in range(index2, index1 - 1, -1):
            self.__data.remove(self.__data[i])

    def update_vector_by_type(self, vector_type, new_color):
        '''
        Function updates the vectors having a given type
        vector_type - integer, new_color - string
        '''
        for vector in self.__data:
            if vector.get_type() == vector_type:
                vector.set_color(new_color)
