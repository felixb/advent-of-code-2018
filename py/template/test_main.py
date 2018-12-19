#! /usr/bin/env python3

import unittest

from main import run_1, run_2


class Test(unittest.TestCase):

    def test_1(self):
        with open('test-1') as f:
            self.assertEqual(1, run_1(f.read()))

    def test_2(self):
        with open('test-1') as f:
            self.assertEqual(None, run_2(f.read()))


if __name__ == '__main__':
    unittest.main()
