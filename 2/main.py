#! /usr/bin/env python3

import sys
from collections import defaultdict


def count_letters(id):
    chars = defaultdict(lambda: 0)
    for char in id:
        chars[char] += 1
    two = 0
    three = 0
    for char, count in chars.items():
        if count == 2:
            two = 1
        elif count == 3:
            three = 1
    return two, three


def run_1(input):
    twos = 0
    threes = 0
    for two, three in [count_letters(id) for id in input.split("\n")]:
        twos += two
        threes += three
    return twos * threes


def diff_id(id1, id2):
    diffs = 0
    same_chars = ''
    for i in range(len(id1)):
        if id1[i] != id2[i]:
            diffs += 1
        else:
            same_chars += id1[i]
    return diffs, same_chars


def run_2(input):
    ids = input.split("\n")
    for id1 in ids:
        results = [same_chars for diff, same_chars in [diff_id(id1, id2) for id2 in ids] if diff == 1]
        if len(results) > 0:
            return results[0]
    return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read().strip()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read().strip()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
