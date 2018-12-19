#! /usr/bin/env python3

import unittest

from main import run_1, run_2


class Test(unittest.TestCase):

    def test_1(self):
        with open('test-1') as f:
            self.assertEqual(6, run_1(f.read()))


if __name__ == '__main__':
    unittest.main()
