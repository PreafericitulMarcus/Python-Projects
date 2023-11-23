from point_logic import MyPoint
import math
import matplotlib.pyplot as plt


def distance_between_two_points(x1, y1, x2, y2):
    """
    Calculates the distance between two point
    x1,y1,x2,y2 integers
    they are the coordinates of 2 points
    returns distance
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class PointRepository:
    def __init__(self):
        """
        this is the list of points
        """
        self.__data = []

    def txt_input(self):
        """
        function reads elements from file input.txt
        enteries are the same as for function add_point_to_repository
        """
        with open("input.txt", "r") as file:
            for line in file:
                x, y, color = line.strip().split(" ")
                self.add_point_to_repository(int(x), int(y), color)

    def add_point_to_repository(self, x, y, c):  # path 1
        """
        functions adds a point to the list of points
        x,y are coordinates and c is color
        appends the point to the list of points
        """
        c = c.lower()
        point = MyPoint(x, y, c)
        self.__data.append(point)

    def get_all_points(self):  # path 2
        """
        function returns all the point that are stored
        """
        return self.__data

    def get_point_at_index(self, index):  # path 3
        """
        function returns a point at a specific index
        index - integer
        return the point at index
        """
        return self.__data[index]

    def get_points_by_color(self, color):  # path 4
        """
        funciton searches the points of the same color and makes a new list of them
        color - string
        return a list of points with same color
        """
        color_list = []
        for elem in self.__data:
            if elem.get_color() == color:
                color_list.append(elem)
        return color_list

    def get_points_in_square(self, up_left_x, up_left_y, length):  # path 5
        """
        function determines which points are inside a square given a point and length
        up_left_x, up_left_y - integers, coordinates of the up left point of a square; length - integer
        function return a list of points that are in the square
        """
        bot_right_x = up_left_x + length
        bot_right_y = up_left_y - length
        points_in_square = []
        for elem in self.__data:
            if (
                up_left_x < elem.get_x() < bot_right_x
                and up_left_y > elem.get_y() > bot_right_y
            ):
                points_in_square.append(elem)
        return points_in_square

    def get_minimum_distance_between_two_points(self):  # path 6
        """
        function determines the minimum distance between all the points in the list of points
        return the minimum distance
        """
        minimum = 10000
        for i in range(len(self.__data)):
            for j in range(i + 1, len(self.__data)):
                distance = distance_between_two_points(
                    self.__data[i].get_x(),
                    self.__data[i].get_y(),
                    self.__data[j].get_x(),
                    self.__data[j].get_y(),
                )
                if distance < minimum:
                    minimum = distance
        return minimum

    def update_point_at_index(
        self, new_point_x, new_point_y, new_point_color, index
    ):  # path 7
        """
        function updates a point at a specific index
        new_point_y, new_point_x - integers; new_point_color - string; index - integer
        """
        new_point = MyPoint(new_point_x, new_point_y, new_point_color)
        self.__data[index] = new_point

    def delete_point_by_index(self, index):  # path 8
        """
        function deletes a point in the list of points at a specific index
        """
        del self.__data[index]

    def delete_points_in_square(self, up_left_x, up_left_y, length):  # path 9
        """
        function deletes points in a square given by up left point and length
        up_left_x, up_left_y - integers, coordinates of the up left point; length - integer
        """
        bot_right_x = up_left_x + length
        bot_right_y = up_left_y - length
        points_to_delete = []
        for elem in self.__data:
            if (
                up_left_x < elem.get_x() < bot_right_x
                and up_left_y > elem.get_y() > bot_right_y
            ):
                points_to_delete.append(elem)
        for point in points_to_delete:
            self.__data.remove(point)

    def plot_points_in_chart(self):  # path 10
        """
        function plots the points in the list of points
        shows the user the points ploted
        """
        for point in self.__data:
            plt.scatter(point.get_x(), point.get_y(), color=point.get_color())
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Scatter Plot of Points")
        plt.show()

    def get_points_in_cercle(self, circleX, circleY, radius):
        """
        function determines the points in a circle
        circleX, circleY - integers, coordinates of the center of the circle; radius - integer
        return a list of points that are in the circle
        """
        list_of_points = []
        for point in self.__data:
            if (
                distance_between_two_points(
                    circleX, circleY, point.get_x(), point.get_y()
                )
            ) < radius:
                list_of_points.append(point)
        return list_of_points

    def update_point_by_coordinates(self, coordX, coordY, new_color):
        """
        function updates a point color by its coordintes
        coordX, coordY - integers; new_color - string
        """
        for point in self.__data:
            if point.get_x() == coordX and point.get_y() == coordY:
                point.set_color(new_color)

    def delete_point_by_coordinates(self, coordX, coordY):
        """
        function deletes points by their coordinates
        coordX, coordY - integers
        """
        for point in self.__data:
            if point.get_x() == coordX and point.get_y() == coordY:
                self.__data.remove(point)
