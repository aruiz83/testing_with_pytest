import unittest
from app.reverse_dict import reverse_dict


class TestReverseDict(unittest.TestCase):
    def test_reverse_dict(self):
        test_cases = [
            {
                "input": {"one": 1, "two": 2, "three": 3},
                "expected_output": {1: "one", 2: "two", 3: "three"},
            },
            {
                "input": {"a": 0, "b": -1, "c": 10},
                "expected_output": {0: "a", -1: "b", 10: "c"},
            },
            {"input": {}, "expected_output": {}},
            {
                "input": {"one": "1", "two": 2, "three": 3},
                "expected_output": None,
            },
            {
                "input": ["not a dictionary"],
                "expected_output": None,
            },
            {
                "input": {"one": 1, "two": "2", "three": 3},
                "expected_output": None,
            },
            {
                "input": {"one": 1, "two": 2, "three": "3"},
                "expected_output": None,
            },
            {
                "input": {"one": 1, "two": 2, 3: "three"},
                "expected_output": None,
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                if not isinstance(test_case["input"], dict):
                    self.assertRaises(
                        TypeError,
                        reverse_dict,
                        test_case["input"],
                    )
                elif not all(
                    isinstance(value, int)
                    for value in test_case["input"].values()
                ):
                    self.assertRaises(
                        ValueError,
                        reverse_dict,
                        test_case["input"],
                    )
                else:
                    self.assertEqual(
                        reverse_dict(test_case["input"]),
                        test_case["expected_output"],
                    )


# Run the tests
if __name__ == '__main__':
    unittest.main()
