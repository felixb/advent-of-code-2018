#! /usr/bin/env python3

import re
import sys
from collections import defaultdict
from time import strptime


def parse(line):
    m = re.search(r'.(\d+-\d+-\d+ \d+:(\d+)). (.+)', line)
    return strptime(m.group(1), '%Y-%m-%d %H:%M'), int(m.group(2)), m.group(3)


def run_1(input):
    guards = defaultdict(lambda: defaultdict(lambda: 0))
    events = sorted([parse(line) for line in input.split("\n")], key=lambda e: e[0])

    current_id = None
    start = None
    for _, minute, message in events:
        m = re.search(r'Guard #(\d+) .*', message)
        if m:
            current_id = int(m.group(1))
        elif message == 'falls asleep':
            start = minute
        elif message == 'wakes up':
            guards[current_id]['id'] = current_id
            guards[current_id]['sum'] += minute - start
            for i in range(start, minute):
                guards[current_id][i] += 1
                count = guards[current_id][i]

                if count > guards[current_id]['most_asleep_minutes']:
                    guards[current_id]['most_asleep_minute'] = i
                    guards[current_id]['most_asleep_minutes'] = count
    most_asleep_guard = [g for g in sorted(guards.values(), key=lambda e: e['sum'])][-1:][0]

    return most_asleep_guard['id'] * most_asleep_guard['most_asleep_minute']


def run_2(input):
    guards = defaultdict(lambda: defaultdict(lambda: 0))
    events = sorted([parse(line) for line in input.split("\n")], key=lambda e: e[0])

    current_id = None
    start = None
    most_asleep_minutes = 0
    most_asleep_minute = 0
    most_asleep_id = 0
    for _, minute, message in events:
        m = re.search(r'Guard #(\d+) .*', message)
        if m:
            current_id = int(m.group(1))
        elif message == 'falls asleep':
            start = minute
        elif message == 'wakes up':
            for i in range(start, minute):
                guards[current_id][i] += 1
                count = guards[current_id][i]

                if count > most_asleep_minutes:
                    most_asleep_minute = i
                    most_asleep_minutes = count
                    most_asleep_id = current_id

    return most_asleep_id * most_asleep_minute


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read().strip()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read().strip()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
