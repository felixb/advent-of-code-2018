#! /usr/bin/env python3

import unittest

from main import run_1, run_2


class Test(unittest.TestCase):

    def test_1(self):
        with open('test-1') as f:
            self.assertEqual(1147, run_1(f.read()))

    def test_2(self):
        with open('test-2') as f:
            self.assertEqual(235220, run_2(f.read(), 1000))


if __name__ == '__main__':
    unittest.main()
