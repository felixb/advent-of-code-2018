#! /usr/bin/env python3

import unittest
from main import run_1, run_2


class Test(unittest.TestCase):
    def test_1(self):
        input = "#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2"
        self.assertEqual(4, run_1(input))

    def test_2(self):
        input = "#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2"
        self.assertEqual(3, run_2(input))


if __name__ == '__main__':
    unittest.main()
