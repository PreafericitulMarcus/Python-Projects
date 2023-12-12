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
        """
        Functino adds the vector with the given scalar
        """
        self.__values += scalar

    def add(self, sum_list):
        """
        Function adds the values of the vector with the values of the given list
        """
        self.__values += sum_list

    def subtract(self, sub_list):
        """
        Function subtracts the values of the vector with the values of the given list
        """
        self.__values -= sub_list

    def multiplication(self, mul_list):
        """
        Function multiplies the values of the vector with the values of the given list
        """
        return self.__values.dot(mul_list)

    def sum_elem_vector(self):
        """
        Function returns the sum of the elements of the vector
        """
        return self.__values.sum()

    def product_elem_vector(self):
        """
        Function returns the product of the elements of the vector
        """
        return self.__values.prod()

    def average_elem_vector(self):
        """
        Function returns the average of the elements of the vector
        """
        return self.__values.mean()

    def minim_elem_vector(self):
        """
        Function returns the minimum of the elements of the vector
        """
        return self.__values.min()

    def maximum_elem_vector(self):
        """
        Function returns the maximum of the elements of the vector
        """
        return self.__values.max()
