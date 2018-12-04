#! /usr/bin/env python3

import sys
from collections import defaultdict
import re


class Claim:
    def __init__(self, input):
        m = re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', input)
        self.id = int(m.group(1))
        self.top_x = int(m.group(2))
        self.top_y = int(m.group(3))
        self.width = int(m.group(4))
        self.height = int(m.group(5))
        self.bottom_x = self.top_x + self.width
        self.bottom_y = self.top_y + self.height

    def __repr__(self):
        return '#%d @ %d,%d: %dx%d' % (self.id, self.top_x, self.top_y, self.width, self.height)

    def overlap(self, other):
        return (self.top_x <= other.top_x < self.bottom_x or other.top_x <= self.top_x < other.bottom_x) and (
                self.top_y <= other.top_y < self.bottom_y or other.top_y <= self.top_y < other.bottom_y)


def run_1(input):
    claims = [Claim(claim) for claim in input.split("\n")]
    field = defaultdict(lambda: 0)
    for claim in claims:
        for x in range(claim.top_x, claim.bottom_x):
            for y in range(claim.top_y, claim.bottom_y):
                field['%d,%d' % (x, y)] += 1
    return len([1 for _, v in field.items() if v > 1])


def run_2(input):
    claims = [Claim(claim) for claim in input.split("\n")]
    candidates = claims[:]
    for c1 in claims:
        for c2 in claims:
            if c1 == c2:
                continue
            if c1.overlap(c2):
                if c1 in candidates:
                    candidates.remove(c1)
                if c2 in candidates:
                    candidates.remove(c2)
                break

    if len(candidates) != 1:
        raise RuntimeError("Found %d candidates, expected 1" % len(candidates))
    return candidates[0].id


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read().strip()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read().strip()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
