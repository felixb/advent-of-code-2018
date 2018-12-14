#! /usr/bin/env python3

import unittest

from main import run_1, run_2


class Test(unittest.TestCase):
    def test_1_1(self):
        input = "\n".join([
            "|",
            "v",
            "|",
            "|",
            "|",
            "^",
            "|",
        ])

        self.assertEqual("0,3", run_1(input))

    def test_1_2(self):
        input = "\n".join([
            '/->-\        ',
            '|   |  /----\\',
            '| /-+--+-\  |',
            '| | |  | v  |',
            '\-+-/  \-+--/',
            '  \------/   ',
        ])

        self.assertEqual("7,3", run_1(input))

    def test_2(self):
        input = "\n".join([
            '/>-<\  ',
            '|   |  ',
            '| /<+-\\',
            '| | | v',
            '\>+</ |',
            '  |   ^',
            '  \<->/',
        ])

        self.assertEqual("6,4", run_2(input))


if __name__ == '__main__':
    unittest.main()
