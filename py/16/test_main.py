#! /usr/bin/env python3

import unittest

from main import run_1, run_2, check_op, mulr, addi, seti, addr


class Test(unittest.TestCase):

    def test_mulr(self):
        self.assertTrue(check_op(([3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1]), mulr))

    def test_addi(self):
        self.assertTrue(check_op(([3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1]), addi))

    def test_addr(self):
        self.assertFalse(check_op(([3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1]), addr))

    def test_seti(self):
        self.assertTrue(check_op(([3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1]), seti))

    def test_1(self):
        input = "\n".join(["Before: [3, 2, 1, 1]",
                           "9 2 1 2",
                           "After:  [3, 2, 2, 1]"])

        self.assertEqual(1, run_1(input))


if __name__ == '__main__':
    unittest.main()
