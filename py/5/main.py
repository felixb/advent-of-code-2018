#! /usr/bin/env python3

import sys
import multiprocessing
import functools


def reverse_caps(c):
    if c == c.lower():
        return c.upper()
    return c.lower()


def reduce(input):
    result = input
    start = 0
    found = True
    while found:
        found = False
        for i in range(start, len(result) - 1):
            if result[i] == reverse_caps(result[i + 1]):
                result = result[:i] + result[i + 2:]
                start = max(0, i - 1)
                found = True
                break
    return result


def run_1(input):
    return len(reduce(input))


def clean(input, char):
    return input.replace(char, '').replace(char.upper(), '')


def run_2(input):
    p = multiprocessing.Pool(processes=8)
    chars = [chr(c) for c in range(ord('a'), ord('z'))]
    reduced = p.map(reduce, [clean(input, c) for c in chars])
    lengths = [len(r) for r in reduced]
    return functools.reduce(min, lengths)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read().strip()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read().strip()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
