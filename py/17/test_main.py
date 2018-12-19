#! /usr/bin/env python3

import unittest
from unittest_data_provider import data_provider

from main import run_1, run_2


class Test(unittest.TestCase):
    cases = lambda: (('test-1', 57), ('test-2', 95))

    @data_provider(cases)
    def test_1(self, fn, o):
        with open(fn) as f:
            self.assertEqual(o, run_1(f.read()))

    def test_2(self):
        with open('test-1') as f:
            self.assertEqual(29, run_2(f.read()))


if __name__ == '__main__':
    unittest.main()
