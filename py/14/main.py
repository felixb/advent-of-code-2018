#! /usr/bin/env python3

import sys


def parse(input):
    return int(input)


def new_receipt(receipts, elves):
    n = receipts[elves[0]] + receipts[elves[1]]
    if n >= 10:
        return [int(n / 10), n % 10]
    else:
        return [n]


def new_position(receipts, p):
    return (p + 1 + receipts[p]) % len(receipts)


def to_s(receipts):
    return "".join([str(j) for j in receipts])


def run_1(input):
    l = parse(input)
    receipts = [3, 7]
    elves = [0, 1]
    for i in range(2, l + 10):
        receipts.extend(new_receipt(receipts, elves))
        elves = [new_position(receipts, e) for e in elves]
    return to_s(receipts[l:l + 10])


def run_2(input):
    receipts = [3, 7]
    receipts_s = to_s(receipts)
    elves = [0, 1]
    l = len(input)
    while True:
        ext = new_receipt(receipts, elves)
        receipts.extend(ext)
        receipts_s += to_s(ext)
        elves = [new_position(receipts, e) for e in elves]
        rl = len(receipts_s)
        if rl >= l:
            try:
                return str(receipts_s.index(input, rl - l))
            except ValueError:
                pass


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read().strip()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read().strip()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
