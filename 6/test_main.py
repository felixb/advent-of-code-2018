#! /usr/bin/env python3

import unittest

from main import run_1, run_2


class Test(unittest.TestCase):
    def test_1(self):
        input = "\n".join([
            "1, 1",
            "1, 6",
            "8, 3",
            "3, 4",
            "5, 5",
            "8, 9"
        ])

        self.assertEqual(17, run_1(input))

    def test_2(self):
        input = "\n".join([
            "1, 1",
            "1, 6",
            "8, 3",
            "3, 4",
            "5, 5",
            "8, 9"
        ])

        self.assertEqual(16, run_2(input, 32))


if __name__ == '__main__':
    unittest.main()
