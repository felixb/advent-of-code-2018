#! /usr/bin/env python3

import sys

DIRECTIONS_INDEX = {'^': 0, '>': 1, 'v': 2, '<': 3}
DIRECTION_DIFF = [(0, -1), (1, 0), (0, 1), (-1, 0)]
INDEX_TO_DIRECTION = ['^', '>', 'v', '<']
TURNS = {
    '\\': [3, 2, 1, 0],
    '/': [1, 0, 3, 2],
}


class CrashError(RuntimeError):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cart:
    def __init__(self, tracks, x, y, direction):
        self.__tracks = tracks
        self.__track_width = len(tracks[0])
        self.__direction = direction
        self.__turns = 0
        self.x = x
        self.y = y

    def __repr__(self):
        return "Cart(%s @ %d,%d)" % (INDEX_TO_DIRECTION[self.__direction], self.x, self.y)

    def index(self):
        return self.x + self.y * self.__track_width

    def __position_ahead(self):
        [dx, dy] = DIRECTION_DIFF[self.__direction]
        return self.x + dx, self.y + dy

    def __track_at(self, x, y):
        return self.__tracks[y][x]

    def __current_track(self):
        return self.__track_at(self.x, self.y)

    def tick(self):
        [self.x, self.y] = self.__position_ahead()
        t = self.__current_track()
        if t == '-' or t == '|':
            pass
        elif t in TURNS:
            self.__direction = TURNS[t][self.__direction]
        elif t == '+':
            self.__direction = (self.__direction + self.__turns - 1) % 4
            self.__turns = (self.__turns + 1) % 3
        else:
            raise RuntimeError('Illegal track for %s: %s' % (self, t))


def parse_tracks(input):
    return input \
        .replace('<', '-') \
        .replace('>', '-') \
        .replace('^', '|') \
        .replace('v', '|') \
        .split("\n")


def parse_carts(input, tracks):
    carts = []
    for y, row in enumerate(input.split("\n")):
        for x, t in enumerate(row):
            if t in DIRECTIONS_INDEX:
                carts.append(Cart(tracks, x, y, DIRECTIONS_INDEX[t]))
    return carts


def parse(input):
    return parse_carts(input, parse_tracks(input))


def tick(carts, i):
    # print("%d: %s" % (i, carts))
    for cart in carts:
        cart.tick()
        if 2 <= len([c.index() for c in carts if c.index() == cart.index()]):
            raise CrashError(cart.x, cart.y)
    return sorted(carts, key=Cart.index)


def run_1(input):
    carts = parse(input)
    try:
        i = 0
        while True:
            carts = tick(carts, i)
            i += 1
    except CrashError as e:
        return "%d,%d" % (e.x, e.y)


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
