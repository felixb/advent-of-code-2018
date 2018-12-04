#! /usr/bin/env python3

import unittest
from main import run_1, run_2


class Test(unittest.TestCase):
    def test_1(self):
        input = "abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab"
        self.assertEqual(run_1(input), 12)

    def test_2(self):
        input = "abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz"
        self.assertEqual(run_2(input), "fgij")


if __name__ == '__main__':
    unittest.main()
