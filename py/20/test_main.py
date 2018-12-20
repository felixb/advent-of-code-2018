#! /usr/bin/env python3

import unittest

from main import run_1, run_2
from unittest_data_provider import data_provider


class Test(unittest.TestCase):
    cases = lambda: (
        ("^WNE$", 3),
        ("^ENWWW(NEEE|SSE(EE|N))$", 10),
        ("^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$", 18),
        ("^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$", 23),
        ("^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$", 31)
    )

    @data_provider(cases)
    def test_1(self, i, o):
        self.assertEqual(o, run_1(i))

    def test_2(self):
        self.assertEqual(None, run_2(""))


if __name__ == '__main__':
    unittest.main()
