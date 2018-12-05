#! /usr/bin/env python3

import unittest
from main import run_1, run_2


class Test(unittest.TestCase):
    def test_1(self):
        inputs = [
            ("aA", 0),
            ("abBA", 0),
            ("abAB", 4),
            ("aabAAB", 6),
            ("dabAcCaCBAcCcaDA", 10),
        ]

        for input, result in inputs:
            self.assertEqual(result, run_1(input), "%s should result in length %d" % (input, result))

    def test_2(self):
        self.assertEqual(4, run_2('dabAcCaCBAcCcaDA'))


if __name__ == '__main__':
    unittest.main()
