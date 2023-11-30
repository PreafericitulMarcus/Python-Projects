import unittest
from vector_logic import MyVector


class TestMyVector(unittest.TestCase):
    def setUp(self):
        self.test_vector = MyVector(0, "r", 2, [1, 1, 1, 1])

    def test_creation(self):
        self.assertListEqual(list(self.test_vector.get_values()), [1, 1, 1, 1])
        self.assertEqual(self.test_vector.get_type(), 2)
        self.assertEqual(self.test_vector.get_color(), "r")
        self.assertEqual(self.test_vector.get_name_id(), 0)

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


if __name__ == "__main__":
    unittest.main()
