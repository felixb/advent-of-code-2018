#! /usr/bin/env python3
import re
import sys
from collections import Counter


def min_max(min_v, max_v, v):
    if min_v:
        return min(min_v, v), max(max_v, v)
    else:
        return v, v


def parse(input):
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    field = {}
    for line in input.split("\n"):
        m = re.search('(.)=(\d+), .=(\d+)..(\d+)', line)
        if m.group(1) == 'x':
            x = int(m.group(2))
            for y in range(int(m.group(3)), int(m.group(4)) + 1):
                field[(x, y)] = '#'
                min_x, max_x = min_max(min_x, max_x, x)
                min_y, max_y = min_max(min_y, max_y, y)
        else:
            y = int(m.group(2))
            for x in range(int(m.group(3)), int(m.group(4)) + 1):
                field[(x, y)] = '#'
                min_x, max_x = min_max(min_x, max_x, x)
                min_y, max_y = min_max(min_y, max_y, y)
    return field, min_x - 1, max_x + 1, min_y, max_y


def free(field, pos):
    return pos not in field or field[pos] == '|'


def falling(field, pos):
    return pos in field and field[pos] == '|'


def blocking(field, pos):
    return pos in field and field[pos] in ['#', '~']


def flow(field, min_x, max_x, min_y, max_y, start):
    x, y = start
    y = max(y, min_y)

    while y < max_y + 1:
        current = (x, y)
        below = (x, y + 1)
        if free(field, current):
            if falling(field, below):
                field[current] = '|'
                return
            if free(field, below):
                field[current] = '|'
                y += 1

            elif blocking(field, below):
                spill = set()
                for d in [-1, +1]:
                    nx, ny = current
                    while min_x <= nx <= max_x and free(field, (nx, ny)):
                        spill.add((nx, ny))
                        if free(field, (nx, ny + 1)):
                            break
                        nx += d
                if spill:
                    bottomless = [(nx, ny) for nx, ny, f in [(x, y, free(field, (x, y + 1))) for x, y in spill] if f]
                    if bottomless:
                        for n in spill:
                            field[n] = '|'
                        for n in bottomless:
                            flow(field, min_x, max_x, min_y, max_y, n)
                        return
                    else:
                        for n in spill:
                            field[n] = '~'
                        y -= 1
        else:
            return


def print_field(field, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in field:
                row += field[(x, y)]
            else:
                row += '.'
        print("%5d" % y, row)


def run_1(input):
    field, min_x, max_x, min_y, max_y = parse(input)
    orig = len(field)
    flow(field, min_x, max_x, min_y, max_y, (500, 0))
    # print_field(field, min_x, max_x, min_y, max_y)
    return len(field) - orig


def run_2(input):
    field, min_x, max_x, min_y, max_y = parse(input)
    flow(field, min_x, max_x, min_y, max_y, (500, 0))
    cnt = Counter(field.values())
    return cnt['~']


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
