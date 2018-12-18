#! /usr/bin/env python3

import unittest

from main import run_1, run_2, parse


class Test(unittest.TestCase):
    def test_1_move_1(self):
        units = parse("\n".join(["G....",
                                 ".....",
                                 "..E..",
                                 ".....",
                                 "...G."]))
        e = [u for u in units if u.type == 'E'][0]
        e.tick(1, units)
        self.assertEqual((3, 2), (e.x, e.y))

    def test_1_move_2(self):
        units = parse("\n".join(["#######",
                                 "#.E...#",
                                 "#.....#",
                                 "#...G.#",
                                 "#######"]))
        e = [u for u in units if u.type == 'E'][0]
        e.tick(1, units)
        self.assertEqual((3, 1), (e.x, e.y))

    def test_1_attack_1(self):
        units = parse("\n".join(["G....",
                                 "..G..",
                                 "..EG.",
                                 "..G..",
                                 "...G."]))
        e = [u for u in units if u.type == 'E'][0]
        r = e.tick(1, units)
        self.assertTrue(r)
        self.assertEqual(197, units[1].hitpoints)

    def test_1_attack_2(self):
        units = parse("\n".join(["G....",
                                 "..G..",
                                 "..EG.",
                                 "..G..",
                                 "...G."]))
        units[3].hitpoints = 10
        e = [u for u in units if u.type == 'E'][0]
        r = e.tick(1, units)
        self.assertTrue(r)
        self.assertEqual(7, units[3].hitpoints)

    def test_1(self):
        cases = {
            "\n".join(["#######",
                       "#.G...#",
                       "#...EG#",
                       "#.#.#G#",
                       "#..G#E#",
                       "#.....#",
                       "#######"]): 27730,
            "\n".join(["#######",
                       "#G..#E#",
                       "#E#E.E#",
                       "#G.##.#",
                       "#...#E#",
                       "#...E.#",
                       "#######"]): 36334,
            "\n".join(["#######",
                       "#E..EG#",
                       "#.#G.E#",
                       "#E.##E#",
                       "#G..#.#",
                       "#..E#.#",
                       "#######"]): 39514,
            "\n".join(["#######",
                       "#E.G#.#",
                       "#.#G..#",
                       "#G.#.G#",
                       "#G..#.#",
                       "#...E.#",
                       "#######"]): 27755,
            "\n".join(["#######",
                       "#.E...#",
                       "#.#..G#",
                       "#.###.#",
                       "#E#G#G#",
                       "#...#G#",
                       "#######"]): 28944,
            "\n".join(["#########",
                       "#G......#",
                       "#.E.#...#",
                       "#..##..G#",
                       "#...##..#",
                       "#...#...#",
                       "#.G...G.#",
                       "#.....G.#",
                       "#########"]): 18740,
        }

        for i, o in cases.items():
            print(i)
            self.assertEqual(o, run_1(i))

    def test_2(self):
        self.assertEqual(None, run_2(input))


if __name__ == '__main__':
    unittest.main()
