import unittest
from vector_logic import MyVector
from vector_repository import VectorRepository


class TestMyVector(unittest.TestCase):
    def setUp(self):
        self.test_vector = MyVector("0", "r", 2, [1, 1, 1, 1])

    def test_creation(self):
        self.assertListEqual(list(self.test_vector.get_values()), [1, 1, 1, 1])
        self.assertEqual(self.test_vector.get_type(), 2)
        self.assertEqual(self.test_vector.get_color(), "r")
        self.assertEqual(self.test_vector.get_name_id(), "0")

    def test_set_get(self):
        self.test_vector.set_color("b")
        self.assertEqual(self.test_vector.get_color(), "b")

    def test_add_scalar(self):
        self.test_vector.add_scalar(4)
        self.assertEqual(list(self.test_vector.get_values()), [5, 5, 5, 5])

    def test_add(self):
        self.test_vector.add([1, 2, 3, 4])
        self.assertEqual(list(self.test_vector.get_values()), [2, 3, 4, 5])

    def test_subtract(self):
        self.test_vector.subtract([1, 2, 3, 4])
        self.assertEqual(list(self.test_vector.get_values()), [0, -1, -2, -3])

    def test_multiplication(self):
        self.test_vector.multiplication([1, 2, 3, 4])
        self.assertEqual(list(self.test_vector.get_values()), [1, 2, 3, 4])

    def test_sum_elem_vector(self):
        self.assertEqual(self.test_vector.sum_elem_vector(), 4)

    def test_product_elem_vector(self):
        self.assertEqual(self.test_vector.product_elem_vector(), 1)

    def test_average_elem_vector(self):
        self.assertEqual(self.test_vector.average_elem_vector(), 1)

    def test_minim_elem_vector(self):
        self.assertEqual(self.test_vector.minim_elem_vector(), 1)

    def test_maximum_elem_vector(self):
        self.assertEqual(self.test_vector.maximum_elem_vector(), 1)

    def test_tearDown(self):
        unittest.TestCase.tearDown(self)


class Test_UI:
    def test_path(path):
        try:
            path = int(path)
            if 0 <= path <= 11:
                return True
            else:
                raise IndexError("Path not found")
        except IndexError as err:
            print("Error:", err)
            return False

    def test_color(color):
        if color in ["r", "g", "b", "y", "m"]:
            return True
        return False

    def test_type(t):
        if t >= 1:
            return True
        else:
            return False


class TestVectorRepository(unittest.TestCase):
    def setUp(self):
        self.vector_repo = VectorRepository()

    def test_add_vector_to_repository(self):
        self.vector_repo.add_vector_to_repository("0", "r", 2, [1, 1, 1, 1])
        self.assertEqual(len(self.vector_repo.get_all_vectors()), 1)
        self.assertEqual(self.vector_repo.get_vector_at_index(0).get_name_id(), "0")
        self.assertEqual(self.vector_repo.get_vector_at_index(0).get_color(), "r")
        self.assertEqual(self.vector_repo.get_vector_at_index(0).get_type(), 2)
        self.assertEqual(
            list(self.vector_repo.get_vector_at_index(0).get_values()), [1, 1, 1, 1]
        )

    def test_update_vector_at_index(self):
        self.vector_repo.add_vector_to_repository("1", "r", 2, [1, 1, 1, 2])
        self.vector_repo.update_vector_at_index(0, "b", 1, [2, 2, 2, 2])
        self.assertEqual(self.vector_repo.get_vector_at_index(0).get_color(), "b")
        self.assertEqual(self.vector_repo.get_vector_at_index(0).get_type(), 1)
        self.assertEqual(
            list(self.vector_repo.get_vector_at_index(0).get_values()), [2, 2, 2, 2]
        )

    def test_vector_at_name_id(self):
        self.vector_repo.add_vector_to_repository("1", "r", 2, [1, 1, 1, 2])
        self.vector_repo.update_vector_at_name_id("1", "b", 1, [2, 2, 2, 2])
        self.assertEqual(self.vector_repo.get_vector_at_index(0).get_color(), "b")
        self.assertEqual(self.vector_repo.get_vector_at_index(0).get_type(), 1)
        self.assertEqual(
            list(self.vector_repo.get_vector_at_index(0).get_values()), [2, 2, 2, 2]
        )

    def test_delete_vector_by_index(self):
        self.vector_repo.add_vector_to_repository("1", "r", 2, [1, 1, 1, 2])
        self.vector_repo.delete_vector_by_index(0)
        self.assertEqual(len(self.vector_repo.get_all_vectors()), 0)

    def test_delete_vector_by_name_id(self):
        self.vector_repo.add_vector_to_repository("1", "r", 2, [1, 1, 1, 2])
        self.vector_repo.delete_vector_by_name_id("1")
        self.assertEqual(len(self.vector_repo.get_all_vectors()), 0)

    def test_plot_vectors_in_chart(self):
        self.vector_repo.add_vector_to_repository("1", "r", 2, [1, 1, 1, 2])
        self.vector_repo.add_vector_to_repository("2", "b", 1, [2, 2, 2, 2])
        self.vector_repo.plot_vectors_in_chart()

    def test_get_vectors_having_sum(self):
        self.vector_repo.add_vector_to_repository("1", "r", 2, [1, 1, 1, 1])
        self.vector_repo.add_vector_to_repository("2", "b", 1, [2, 2, 2, 2])
        self.assertEqual(len(self.vector_repo.get_vectors_having_sum(4)), 1)

    def test_delete_vector_between_indexes(self):
        self.vector_repo.add_vector_to_repository("1", "r", 2, [1, 1, 1, 1])
        self.vector_repo.add_vector_to_repository("2", "b", 1, [2, 2, 2, 2])
        self.vector_repo.delete_vectors_between_indexes(0, 1)
        self.assertEqual(len(self.vector_repo.get_all_vectors()), 0)

    def test_update_vector_by_type(self):
        self.vector_repo.add_vector_to_repository("1", "r", 2, [1, 1, 1, 1])
        self.vector_repo.add_vector_to_repository("2", "b", 1, [2, 2, 2, 2])
        self.vector_repo.update_vector_by_type(1, "g")
        self.assertEqual(self.vector_repo.get_vector_at_index(0).get_color(), "r")
        self.assertEqual(self.vector_repo.get_vector_at_index(1).get_color(), "g")


if __name__ == "__main__":
    unittest.main()
