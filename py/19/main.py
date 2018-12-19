#! /usr/bin/env python3

import sys


def addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]


def addi(regs, a, b, c):
    regs[c] = regs[a] + b


def mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]


def muli(regs, a, b, c):
    regs[c] = regs[a] * b


def banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]


def bani(regs, a, b, c):
    regs[c] = regs[a] & b


def borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]


def bori(regs, a, b, c):
    regs[c] = regs[a] | b


def setr(regs, a, b, c):
    regs[c] = regs[a]


def seti(regs, a, b, c):
    regs[c] = a


def gtir(regs, a, b, c):
    if a > regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0


def gtri(regs, a, b, c):
    if regs[a] > b:
        regs[c] = 1
    else:
        regs[c] = 0


def gtrr(regs, a, b, c):
    if regs[a] > regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0


def eqir(regs, a, b, c):
    if a == regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0


def eqri(regs, a, b, c):
    if regs[a] == b:
        regs[c] = 1
    else:
        regs[c] = 0


def eqrr(regs, a, b, c):
    if regs[a] == regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0


def exec(ipr, ip, regs, line):
    regs[ipr] = ip
    op = OP_CODES[line[0]]
    op(regs, *line[1:])
    return regs[ipr] + 1


OP_CODES = {'addr': addr, 'addi': addi,
            'mulr': mulr, 'muli': muli,
            'banr': banr, 'bani': bani,
            'borr': borr, 'bori': bori,
            'setr': setr, 'seti': seti,
            'gtri': gtri, 'gtir': gtir, 'gtrr': gtrr,
            'eqri': eqri, 'eqir': eqir, 'eqrr': eqrr}


def parse_line(line):
    parts = line.split(' ')
    return parts[0], int(parts[1]), int(parts[2]), int(parts[3])


def parse(input):
    lines = input.split("\n")
    ipr = int(lines[0][4])
    program = [parse_line(l) for l in lines[1:]]
    return ipr, program


def run(input, init=0):
    ipr, program = parse(input)
    ip = 0
    regs = [init, 0, 0, 0, 0, 0]
    while ip < len(program):
        ip = exec(ipr, ip, regs, program[ip])
    return regs[0]


def run_1(input):
    return run(input)


def run_2(input):
    return run(input, 1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
