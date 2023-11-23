class MyPoint:
    def __init__(self, coord_x, coord_y, color):
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__color = color

    def __str__(self):
        return f"Point ({self.__coord_x}, {self.__coord_y}) of color {self.__color}"

    def get_x(self):
        return self.__coord_x

    def get_y(self):
        return self.__coord_y

    def get_color(self):
        return self.__color

    def set_x(self, new_coord_x):
        self.__coord_x = new_coord_x

    def set_y(self, new_coord_y):
        self.__coord_y = new_coord_y

    def set_color(self, new_color):
        self.__color = new_color
