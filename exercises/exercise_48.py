import unittest
from app.calculate_shipping_cost import calculate_shipping_cost


# Enter your solution here
class TestCalculateShippingCost(unittest.TestCase):
    def test_non_numeric_weight(self):
        with self.assertRaises(TypeError):
            calculate_shipping_cost("5kg", "USA")
        with self.assertRaisesRegex(
            TypeError, "Weight must be a number"
        ):
            calculate_shipping_cost("5", "USA")

    def test_non_positive_weight(self):
        with self.assertRaises(ValueError):
            calculate_shipping_cost(-10, "USA")
        with self.assertRaisesRegex(
            ValueError, "Weight must be greater than zero"
        ):
            calculate_shipping_cost(-100, "USA")

    def test_non_string_destination(self):
        with self.assertRaises(TypeError):
            calculate_shipping_cost(10, True)

        with self.assertRaises(TypeError):
            calculate_shipping_cost(10, 10)

        with self.assertRaisesRegex(
            TypeError, "Destination must be a string"
        ):
            calculate_shipping_cost(100, 50)

    def test_empty_destination(self):
        with self.assertRaises(ValueError):
            calculate_shipping_cost(10, "")

        with self.assertRaisesRegex(
            ValueError, "Destination cannot be empty"
        ):
            calculate_shipping_cost(100, "")


# Run the tests
if __name__ == '__main__':
    unittest.main()
