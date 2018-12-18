#! /usr/bin/env python3
import sys

DIRECTIONS = [(0, -1), (-1, 0), (1, 0), (0, 1)]


class Pathfinder:
    def __init__(self, field, units, start, targets):
        self.__field_width = len(field[0])
        self.__field_height = len(field)
        self.__field = [row[:] for row in field]
        self.__start = start
        self.__targets = targets
        for u in units:
            self.__field[u.y][u.x] = False
        self.__first = [(x, y) for x, y in [(self.__start[0] + dx, self.__start[1] + dy) for dx, dy in DIRECTIONS] if
                        self.__valid(x, y)]

    def find_best(self):
        for f in self.__first:
            if f in self.__targets:
                return f

        i = 0
        dists = {}
        current = []
        for t in self.__targets:
            dists[t] = 0
            current.append(t)

        while True:
            i += 1
            old = current
            current = []
            for c in old:
                for x, y in [(c[0] + dx, c[1] + dy) for dx, dy in DIRECTIONS]:
                    if self.__valid(x, y) and self.__field[y][x] and (x, y) not in dists:
                        dists[(x, y)] = i
                        current.append((x, y))
            if not current:
                return None
            for f in self.__first:
                if f in current:
                    return f

    def __valid(self, x, y):
        return 0 <= x < self.__field_width \
               and 0 <= y < self.__field_height \
               and self.__field[y][x]


class Unit:
    def __init__(self, field, type, x, y):
        self.__field = field
        self.__field_width = len(field[0])
        self.__field_height = len(field)
        self.__power = 3
        self.type = type
        self.ticks = None
        self.hitpoints = 200
        self.x = x
        self.y = y

    def __repr__(self):
        return "%s(%d,%dx%d)" % (self.type, self.hitpoints, self.x, self.y)

    def index(self):
        return index_of(self.__field_width, self.x, self.y)

    def tick(self, i, units):
        self.ticks = i
        if self.__attack(units):
            return True
        self.__move(units)
        return self.__attack(units)

    def __attack(self, units):
        enemies = [e for e in [self.__enemy_at(units, self.x + dx, self.y + dy) for dx, dy in DIRECTIONS] if e]
        if not enemies:
            return False
        min_hitpoints = min([e.hitpoints for e in enemies])
        enemy = sorted([e for e in enemies if e.hitpoints == min_hitpoints], key=Unit.index)[0]
        enemy.hitpoints -= self.__power
        return True

    def __move(self, units):
        pf = Pathfinder(self.__field, units, (self.x, self.y), self.__targets(units))
        f = pf.find_best()
        if f:
            self.x, self.y = f

    def __unit_at(self, units, x, y):
        result = [u for u in units if u.x == x and u.y == y]
        if result:
            return result[0]
        else:
            return None

    def __wall_at(self, x, y):
        return x < 0 \
               or x >= self.__field_width \
               or y < 0 \
               or y >= self.__field_height \
               or not self.__field[y][x]

    def __free_at(self, units, x, y):
        return not self.__wall_at(x, y) and self.__unit_at(units, x, y) is None

    def __enemy_at(self, units, x, y):
        u = self.__unit_at(units, x, y)
        if u and u.type != self.type:
            return u
        else:
            return None

    def __enemies(self, units):
        return [u for u in units if u.type != self.type]

    def __targets(self, units):
        targets = set()
        for e in self.__enemies(units):
            for dx, dy in DIRECTIONS:
                x = e.x + dx
                y = e.y + dy
                if self.__free_at(units, x, y):
                    targets.add((x, y))
        return list(targets)


def index_of(l, x, y):
    return x + y * l


def range_to(p0, p1):
    if p0 < p1:
        return range(p0 + 1, p1 + 1)
    else:
        return reversed(range(p1, p0))


def parse_field(input):
    parsed = input \
        .replace('E', '.') \
        .replace('G', '.') \
        .split("\n")
    return [[f == '.' for f in row] for row in parsed]


def parse_units(input, field):
    units = []
    for y, row in enumerate(input.split("\n")):
        for x, f in enumerate(row):
            if f in ['G', 'E']:
                units.append(Unit(field, f, x, y))
    return units


def parse(input):
    return parse_units(input, parse_field(input))


def tick(units, i):
    for unit in [u for u in units if u.ticks != i]:
        if unit.tick(i, units):
            new_units = [u for u in units if u.hitpoints > 0]
            if len(new_units) < len(units):
                return new_units
    return sorted(units, key=Unit.index)


def b_to_f(b):
    if b:
        return '.'
    else:
        return '#'


def run_1(input):
    i = 0
    field = parse_field(input)
    units = parse_units(input, field)
    while len(set([u.type for u in units])) > 1:
        for y, row in enumerate(field):
            row = [b_to_f(b) for b in row]
            for u in [u for u in units if u.y == y]:
                row[u.x] = u.type
            s = ""
            for f in row:
                s += f
        units = tick(units, i)
        if not [u for u in units if u.ticks != i]:
            i += 1
    return i * sum([u.hitpoints for u in units])


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
