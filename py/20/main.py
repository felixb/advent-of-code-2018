#! /usr/bin/env python3
import re
import sys


def parse(input):
    return input[1:-1]


def expand(input):
    longest = input

    while '|)' in longest:
        longest = re.sub('\([NSEW|]*\|\)', '', longest)

    while '|' in longest:
        m = re.search('\([NSEW|]*\)', longest)
        s = m.start(0)
        e = m.end(0)
        prefix = longest[:s]
        suffix = longest[e:]
        splits = longest[s + 1:e - 1].split('|')
        middle = sorted(splits, key=len)[-1]
        longest = prefix + middle + suffix
    return longest


def run_1(input):
    longest = expand(parse(input))
    return len(longest)


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
