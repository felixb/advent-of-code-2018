#! /usr/bin/env python3

import unittest

from main import run_1, run_2


class Test(unittest.TestCase):
    def test_1(self):
        cases = {
            '5': "0124515891",
            '9': "5158916779",
            '18': "9251071085",
            '2018': "5941429882",
        }

        for i, o in cases.items():
            self.assertEqual(o, run_1(i), 'failed with input %s' % i)

    def test_2(self):
        self.assertEqual(None, run_2("5"))


if __name__ == '__main__':
    unittest.main()
