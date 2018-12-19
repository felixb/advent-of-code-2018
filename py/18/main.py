#! /usr/bin/env python3

import sys
from collections import Counter


def init_directions():
    d = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x != 0 or y != 0:
                d.append((x, y))
    return d


def enum_directions(width, height, x, y):
    return [(x0, y0) for x0, y0 in [(x + dx, y + dy) for dx, dy in DIRECTIONS] if 0 <= x0 < width and 0 <= y0 < height]


DIRECTIONS = init_directions()


def parse(input):
    field = {}
    width = 0
    height = 0
    for y, row in enumerate(input.split("\n")):
        for x, f in enumerate(row):
            field[(x, y)] = f
            width = max(width, x + 1)
        height = max(height, y + 1)
    return field, width, height


def adjacents(field, width, height, x, y):
    return Counter([field[p] for p in enum_directions(width, height, x, y)])


def tick(field, width, height):
    new_field = {}
    for y in range(height):
        for x in range(width):
            f = field[(x, y)]

            c = adjacents(field, width, height, x, y)
            if f == '.' and c.get('|', 0) >= 3:
                new_field[(x, y)] = '|'
            elif f == '|' and c.get('#', 0) >= 3:
                new_field[(x, y)] = '#'
            elif f == '#' and (c.get('#', 0) == 0 or c.get('|', 0) == 0):
                new_field[(x, y)] = '.'
            else:
                new_field[(x, y)] = f

    return new_field


def print_field(field, height, width):
    print()
    c = Counter(field.values())
    print(c['#'] * c['|'])
    for y in range(height):
        row = ""
        for x in range(width):
            row += field[(x, y)]
        print(row)


def field_to_s(field, width, height):
    s = ""
    for y in range(height):
        for x in range(width):
            s += field[(x, y)]
    return s


def ticks(input, minutes):
    field, width, height = parse(input)
    # print_field(field, height, width)

    i = 0
    fields = {}
    while i < minutes:
        new_field = tick(field, width, height)
        s = field_to_s(new_field, width, height)
        if s in fields:
            old = fields[s]
            diff = i - old
            if i + diff < minutes:
                i += diff
                continue
        field = new_field
        fields[s] = i
        i += 1

    c = Counter(field.values())
    return c['#'] * c['|']


def run_1(input):
    return ticks(input, 10)


def run_2(input, minutes=1000000000):
    return ticks(input, minutes)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
