#! /usr/bin/env python3

import sys


def run_1(input):
    result = 0
    for c in [int(e) for e in input.split("\n")]:
        result += c
    return result


def run_2(input):
    result = 0
    frequencies = {result}
    changes = [int(e) for e in input.split("\n")]
    while True:
        for c in changes:
            result += c
            if result in frequencies:
                return result
            frequencies.add(result)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read().strip()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read().strip()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
