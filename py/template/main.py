#! /usr/bin/env python3

import sys


def parse(input):
    return input


def run_1(input):
    return parse(input)


def run_2(input):
    return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
