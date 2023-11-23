from point_repository import PointRepository
from test_point import Test

test = Test()


def menu():
    print(
        """
1. Add a point to the repository
2. Get all points
3. Get a point at a given index
4. Get a point of a given color
5. Get all points that are inside a given square(up-left corner and length given)
6. Get the minimum distance between two points
7. Update a point at a given index
8. Delete a point by index
9. Delete all points that are inside a given square
10. Plot all points in a chart (using library matplotib)
12. Get points that are in a given circle 
12. Update color of a point given coordinates 
13. Delete a point by coordinates
0. Exit
"""
    )

    point_repo = PointRepository()
    point_repo.txt_input()
    ok = True
    while ok == True:
        path = input("\nWhat path do you want to go?: ")
        if test.check_path(path):
            path = int(path)

            if path == 0:
                ok = False
                print("exit...")

            elif path == 1:  # path 1
                try:
                    coordinate_x = int(input("Value for x: "))
                    coordinate_y = int(input("Value for y: "))
                    color_point = input("Color of the point: ")

                    if test.test_color(color_point):
                        point_repo.add_point_to_repository(
                            coordinate_x, coordinate_y, color_point
                        )
                    else:
                        raise ValueError("color not in set")
                except ValueError as err:
                    print("Error:", err)

            elif path == 2:  # path2
                all_points = point_repo.get_all_points()
                for point in all_points:
                    print(point)

            elif path == 3:  # path 3
                try:
                    index = int(input("The point with what index do you want?: "))
                    print(point_repo.get_point_at_index(index))
                except (IndexError, ValueError) as err:
                    print("error:", err)

            elif path == 4:  # path 4
                try:
                    choose_color = input("The color to search the points by: ")
                    choose_color = choose_color.lower()
                    if not test.test_color(choose_color):
                        raise ValueError("color not in set")
                    points_by_color = point_repo.get_points_by_color(choose_color)
                    for point in points_by_color:
                        print(point)
                except ValueError as err:
                    print("error:", err)

            elif path == 5:  # path 5
                try:
                    up_left = input("coordonates of the upper left corrner (x y): ")
                    up_left_x, up_left_y = up_left.strip().split(" ")
                    up_left_x = int(up_left_x)
                    up_left_y = int(up_left_y)
                    length = int(input("what is the length: "))
                    points = point_repo.get_points_in_square(
                        up_left_x, up_left_y, length
                    )
                    for point in points:
                        print(point)
                except (IndexError, ValueError) as err:
                    print("Error:", err)

            elif path == 6:  # path 6
                print(point_repo.get_minimum_distance_between_two_points())

            elif path == 7:  # path 7
                try:
                    index = input("Enter the index of the point to update: ")
                    index = int(index)
                    new_coordinate_x = input("Enter new x coordinate: ")
                    new_coordinate_y = input("Enter new y coordinate: ")
                    new_coordinate_x = int(new_coordinate_x)
                    new_coordinate_y = int(new_coordinate_y)
                    new_color = input("Enter new color: ")
                    new_color = new_color.lower()
                    if not test.test_color(new_color):
                        raise ValueError("color not in set")
                    point_repo.update_point_at_index(
                        new_coordinate_x, new_coordinate_y, new_color, index
                    )
                except (ValueError, IndexError) as err:
                    print("Error:", err)

            elif path == 8:  # path 8
                try:
                    index = int(input("Index for the point to be deleted: "))
                    point_repo.delete_point_by_index(index)
                except (IndexError, ValueError) as err:
                    print("Error:", err)

            elif path == 9:  # path 9
                try:
                    up_left = input("coordonates of the upper left corrner (x y): ")
                    up_left_x, up_left_y = up_left.strip().split(" ")
                    up_left_x = int(up_left_x)
                    up_left_y = int(up_left_y)
                    length = int(input("what is the length: "))
                    points = point_repo.delete_points_in_square(
                        up_left_x, up_left_y, length
                    )
                except (IndexError, ValueError) as err:
                    print("Error:", err)

            elif path == 10:  # path 10
                point_repo.plot_points_in_chart()

            elif path == 11:
                try:
                    circle_x = int(input("x for center: "))
                    circle_y = int(input("y for center: "))
                    radius = int(input("input radius of the circle: "))
                    list_of_points = point_repo.get_points_in_cercle(
                        circle_x, circle_y, radius
                    )
                    for point in list_of_points:
                        print(point)
                except (ValueError, IndexError) as err:
                    print("Error:", err)

            elif path == 12:
                try:
                    x = int(input("coordinates for x: "))
                    y = int(input("coordinates for y: "))
                    new_color = input("What is the new color: ")
                    new_color = new_color.lower()
                    if not test.test_color(new_color):
                        raise ValueError("color not in set")
                    point_repo.update_point_by_coordinates(x, y, new_color)
                except (ValueError, IndexError) as err:
                    print("Error:", err)

            elif path == 13:
                try:
                    x = int(input("coordinates for x: "))
                    y = int(input("coordinates for y: "))
                    point_repo.delete_point_by_coordinates(x, y)
                except (ValueError, IndexError) as err:
                    print("Error", err)


menu()
