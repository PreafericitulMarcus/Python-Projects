import numpy as np

# TODO getter, setter, change the vector(add vecotr, substract...)
# test each def


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

    # only test
    def add_scalar(self, scalar):
        pass

    def add(self, list):
        pass

    def subtract(self, list):
        pass

    def multiplication(self, list):
        pass

    def sum_elem_vector(self):
        pass
