#! /usr/bin/env python3

import unittest
from main import run_1, run_2


class Test(unittest.TestCase):
    def test_1(self):
        test_data = [
            ("+1\n-2\n+3\n+1", 3),
            ("+1\n+1\n+1", 3),
            ("+1\n+1\n-2", 0),
            ("-1\n-2\n-3", -6),
        ]

        for input, output in test_data:
            self.assertEqual(run_1(input), output)

    def test_2(self):
        test_data = [
            ("+1\n-1", 0),
            ("+3\n+3\n+4\n-2\n-4", 10),
            ("-6\n+3\n+8\n+5\n-6", 5),
            ("+7\n+7\n-2\n-7\n-4", 14),
        ]

        for input, output in test_data:
            self.assertEqual(run_2(input), output)


if __name__ == '__main__':
    unittest.main()
