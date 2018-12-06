#! /usr/bin/env python3

import sys
from collections import defaultdict


def parse_line(line):
    x, y = line.split(", ")
    return int(x), int(y)


def parse(input):
    return [parse_line(line) for line in input.split("\n")]


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def closest(x, y, coordinates):
    dists = [dist((x, y), c) for c in coordinates]
    min_dist = min(dists)
    if len([d for d in dists if d == min_dist]) == 1:
        for i in range(len(dists)):
            if dists[i] == min_dist:
                return i
    return -1


def fill_field(coordinates, max_x, max_y):
    field = []
    for x in range(max_x):
        field.append([-1] * max_y)
        for y in range(max_y):
            field[x][y] = closest(x, y, coordinates)
    return field


def find_infinites(field, max_x, max_y):
    infinites = set()
    for x in range(max_x):
        infinites.add(field[x][0])
        infinites.add(field[x][max_y - 1])
    for y in range(max_y):
        infinites.add(field[0][y])
        infinites.add(field[max_x - 1][y])
    infinites.remove(-1)
    return infinites


def max_fields(field):
    result = defaultdict(lambda: 0)
    for x, row in enumerate(field):
        for y, id in enumerate(row):
            if id >= 0:
                result[id] += 1
    return result


def run_1(input):
    coordinates = parse(input)
    max_x = max([c[0] for c in coordinates]) + 1
    max_y = max([c[1] for c in coordinates]) + 1
    field = fill_field(coordinates, max_x, max_y)
    infinites = find_infinites(field, max_x, max_y)
    field_sizes = max_fields(field)
    best_size = 0
    for i, v in field_sizes.items():
        if i not in infinites and v > best_size:
            best_size = v
    return best_size


def fill_field_max_dist(coordinates, max_x, max_y, max_dist):
    field = []
    for x in range(max_x):
        field.append([0] * max_y)
        for y in range(max_y):
            if sum([dist((x, y), c) for c in coordinates]) < max_dist:
                field[x][y] = 1
    return field


def run_2(input, max_dist=10000):
    coordinates = parse(input)
    max_x = max([c[0] for c in coordinates]) + 1
    max_y = max([c[1] for c in coordinates]) + 1
    field = fill_field_max_dist(coordinates, max_x, max_y, max_dist)
    return sum([p for row in field for p in row])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read().strip()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read().strip()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
