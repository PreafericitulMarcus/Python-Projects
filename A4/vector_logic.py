import numpy as np


class MyVector:
    def __init__(self, name_id, color, type, values):
        self.__name_id = name_id
        self.__color = str(color)
        self.__type = type
        self.__values = np.array(values)

    def get_name_id(self):
        return self.__name_id

    def get_color(self):
        return self.__color

    def get_type(self):
        return self.__type

    def get_values(self):
        return self.__values

    def set_name_id(self, new_name_id):
        self.__name_id = new_name_id

    def set_color(self, new_color):
        self.__color = new_color

    def set_type(self, new_type):
        self.__type = new_type

    def set_values(self, new_values):
        self.__values = new_values

    def __str__(self):
        return f"Vector: {self.__name_id}, color: {self.__color}, type: {self.__type}, values: {self.__values}"

    def add_scalar(self, scalar):
        self.__values += scalar

    def add(self, sum_list):
        """
        Function adds the values of the vector with the values of the given list
        """
        for i in range(len(self.__values)):
            self.__values[i] += sum_list[i]

    def subtract(self, sub_list):
        """
        Function subtracts the values of the vector with the values of the given list
        """
        for i in range(len(self.__values)):
            self.__values[i] -= sub_list[i]

    def multiplication(self, mul_list):
        """
        Function multiplies the values of the vector with the values of the given list
        """
        for i in range(len(self.__values)):
            self.__values[i] *= mul_list[i]

    def sum_elem_vector(self):
        """
        Function returns the sum of the elements of the vector
        """
        sum_elem = 0
        for elem in self.__values:
            sum_elem += elem
        return sum_elem

    def product_elem_vector(self):
        """
        Function returns the product of the elements of the vector
        """
        prod_elem = 1
        for elem in self.__values:
            prod_elem *= elem
        return prod_elem

    def average_elem_vector(self):
        """
        Function returns the average of the elements of the vector
        """
        sum_elem = self.sum_elem_vector()
        return sum_elem // len(self.__values)

    def minim_elem_vector(self):
        """
        Function returns the minimum of the elements of the vector
        """
        minimum = self.__values[0]
        for elem in self.__values:
            if elem < minimum:
                minimum = elem
        return minimum

    def maximum_elem_vector(self):
        """
        Function returns the maximum of the elements of the vector
        """
        maximum = self.__values[0]
        for elem in self.__values:
            if elem > maximum:
                maximum = elem
        return maximum
