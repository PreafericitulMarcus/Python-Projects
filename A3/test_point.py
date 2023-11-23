import unittest
from point_repository import PointRepository


class Test(unittest.TestCase):
    def check_path(self, path):
        try:
            path = int(path)
            if 0 <= path <= 13:
                return True
            else:
                raise ValueError("Invalid path value")
        except ValueError as err:
            print("Error:", err)
            return False

    def test_color(self, c):
        """
        Funtion test_color checks to see if the entry color is between the colors accepted
        c - can be any variable
        return True if the color is ok, False otherwise
        """
        c = str(c)
        good_colors = ["red", "green", "blue", "magenta", "yellow"]
        c = c.lower()
        if c in good_colors:
            return True
        else:
            return False

    def test_add_point(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(10, 10, "red")
        self.assertEqual(len(point_repo.get_points()), 1)
        self.assertEqual(point_repo.get_point_at_index(0).get_x(), 10)
        self.assertEqual(point_repo.get_point_at_index(0).get_y(), 10)

    def test_get_points_by_color(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(10, 10, "red")
        point_repo.add_point_to_repository(20, 20, "blue")
        point_repo.add_point_to_repository(30, 30, "red")

        red_points = point_repo.get_points_by_color("red")
        self.assertEqual(len(red_points), 2)
        self.assertEqual(red_points[0].get_x(), 10)
        self.assertEqual(red_points[1].get_x(), 30)

        blue_points = point_repo.get_points_by_color("blue")
        self.assertEqual(len(blue_points), 1)
        self.assertEqual(blue_points[0].get_y(), 20)

    def test_delete_point_by_coordinates(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(10, 10, "red")
        point_repo.add_point_to_repository(20, 20, "blue")
        point_repo.add_point_to_repository(30, 30, "red")

        point_repo.delete_point_by_coordinates(20, 20)
        self.assertEqual(len(point_repo.get_all_points()), 2)
        self.assertEqual(point_repo.get_all_points()[0].get_x(), 10)
        self.assertEqual(point_repo.get_all_points()[1].get_y(), 30)

        point_repo.delete_point_by_coordinates(10, 10)
        self.assertEqual(len(point_repo.get_all_points()), 1)
        self.assertEqual(point_repo.get_all_points()[0].get_x(), 30)

    def test_get_all_points(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(10, 10, "red")
        point_repo.add_point_to_repository(20, 20, "blue")
        point_repo.add_point_to_repository(30, 30, "green")

        all_points = point_repo.get_all_points()
        self.assertEqual(len(all_points), 3)
        self.assertEqual(all_points[0].get_x(), 10)
        self.assertEqual(all_points[1].get_y(), 20)
        self.assertEqual(all_points[2].get_color(), "green")

    def test_get_point_at_index(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(10, 10, "red")
        point_repo.add_point_to_repository(20, 20, "blue")
        point_repo.add_point_to_repository(30, 30, "green")

        point_at_index_1 = point_repo.get_point_at_index(1)
        self.assertEqual(point_at_index_1.get_x(), 20)
        self.assertEqual(point_at_index_1.get_y(), 20)
        self.assertEqual(point_at_index_1.get_color(), "blue")

        point_at_index_2 = point_repo.get_point_at_index(2)
        self.assertEqual(point_at_index_2.get_x(), 30)
        self.assertEqual(point_at_index_2.get_y(), 30)
        self.assertEqual(point_at_index_2.get_color(), "green")

    def test_get_points_in_square(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(5, 5, "red")
        point_repo.add_point_to_repository(15, 15, "blue")
        point_repo.add_point_to_repository(25, 25, "green")

        points_in_square = point_repo.get_points_in_square(0, 20, 20)
        self.assertEqual(len(points_in_square), 2)
        self.assertEqual(points_in_square[0].get_x(), 5)
        self.assertEqual(points_in_square[1].get_color(), "blue")

        points_in_square_2 = point_repo.get_points_in_square(10, 30, 20)
        self.assertEqual(len(points_in_square_2), 1)
        self.assertEqual(points_in_square_2[0].get_y(), 25)

    def test_get_minimum_distance_between_two_points(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(0, 0, "red")
        point_repo.add_point_to_repository(3, 4, "blue")
        point_repo.add_point_to_repository(5, 12, "green")

        min_distance = point_repo.get_minimum_distance_between_two_points()
        self.assertEqual(min_distance, 5)

        point_repo.add_point_to_repository(10, 10, "yellow")
        min_distance_2 = point_repo.get_minimum_distance_between_two_points()
        self.assertEqual(min_distance_2, 5)

    def test_update_point_at_index(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(10, 10, "red")
        point_repo.add_point_to_repository(20, 20, "blue")
        point_repo.add_point_to_repository(30, 30, "green")

        point_repo.update_point_at_index(1, 25, 25, "yellow")
        updated_point = point_repo.get_point_at_index(1)
        self.assertEqual(updated_point.get_x(), 25)
        self.assertEqual(updated_point.get_y(), 25)
        self.assertEqual(updated_point.get_color(), "yellow")

        point_repo.update_point_at_index(0, 15, 15, "red")
        updated_point_2 = point_repo.get_point_at_index(0)
        self.assertEqual(updated_point_2.get_x(), 15)
        self.assertEqual(updated_point_2.get_y(), 15)
        self.assertEqual(updated_point_2.get_color(), "red")

    def test_delete_point_by_index(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(10, 10, "red")
        point_repo.add_point_to_repository(20, 20, "blue")
        point_repo.add_point_to_repository(30, 30, "green")

        point_repo.delete_point_by_index(1)
        self.assertEqual(len(point_repo.get_all_points()), 2)
        self.assertEqual(point_repo.get_all_points()[1].get_color(), "green")

        point_repo.delete_point_by_index(0)
        self.assertEqual(len(point_repo.get_all_points()), 1)
        self.assertEqual(point_repo.get_all_points()[0].get_x(), 30)

    def test_delete_points_in_square(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(5, 5, "red")
        point_repo.add_point_to_repository(15, 15, "blue")
        point_repo.add_point_to_repository(25, 25, "green")

        point_repo.delete_points_in_square(0, 20, 20)
        self.assertEqual(len(point_repo.get_all_points()), 1)
        self.assertEqual(point_repo.get_all_points()[0].get_color(), "red")

        point_repo.delete_points_in_square(10, 30, 20)
        self.assertEqual(len(point_repo.get_all_points()), 0)

    def test_plot_points_in_chart(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(5, 5, "red")
        point_repo.add_point_to_repository(15, 15, "blue")
        point_repo.add_point_to_repository(25, 25, "green")

        # visual test
        point_repo.plot_points_in_chart()

    def test_get_points_in_cercle(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(0, 0, "red")
        point_repo.add_point_to_repository(3, 4, "blue")
        point_repo.add_point_to_repository(5, 12, "green")

        cercle_points = point_repo.get_points_in_cercle(0, 0, 5)
        self.assertEqual(len(cercle_points), 2)
        self.assertEqual(cercle_points[0].get_x(), 3)
        self.assertEqual(cercle_points[1].get_color(), "green")

        cercle_points_2 = point_repo.get_points_in_cercle(0, 0, 1)
        self.assertEqual(len(cercle_points_2), 1)
        self.assertEqual(cercle_points_2[0].get_y(), 4)

    def test_update_point_by_coordinates(self):
        point_repo = PointRepository()
        point_repo.add_point_to_repository(10, 10, "red")
        point_repo.add_point_to_repository(20, 20, "blue")
        point_repo.add_point_to_repository(30, 30, "green")

        point_repo.update_point_by_coordinates(20, 20, "yellow")
        updated_point = point_repo.get_point_at_index(1)
        self.assertEqual(updated_point.get_color(), "yellow")

        point_repo.update_point_by_coordinates(10, 10, "red")
        updated_point_2 = point_repo.get_point_at_index(0)
        self.assertEqual(updated_point_2.get_color(), "red")

    print("successful...")
