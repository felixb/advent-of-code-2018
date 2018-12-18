#! /usr/bin/env python3
import sys
from collections import defaultdict


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


OPS = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtri, gtir, gtrr, eqri, eqir, eqrr]


def parse(input):
    lines = input.split("\n")
    examples = []
    program = []
    i = 0

    while i < len(lines):
        if "Before:" not in lines[i]:
            break
        examples.append((
            [int(i) for i in lines[i][9:].replace(',', '').replace(']', '').split(" ")],
            [int(i) for i in lines[i + 1].split(" ")],
            [int(i) for i in lines[i + 2][9:].replace(',', '').replace(']', '').split(" ")]))
        i += 4

    for l in lines[i:]:
        if l:
            program.append([int(i) for i in l.split(" ")])

    return examples, program


def check_op(ex, op):
    regs = ex[0][:]
    op(regs, *ex[1][1:])
    return regs == ex[2]


def exec(op_codes, regs, line):
    op = op_codes[line[0]]
    op(regs, *line[1:])


def run_1(input):
    examples, _ = parse(input)
    cnt = 0
    for ex in examples:
        if len([1 for r in [check_op(ex, op) for op in OPS] if r]) >= 3:
            cnt += 1
    return cnt


def check_and_add(op_codes, code, op):
    if code in op_codes and op != op_codes[code]:
        raise RuntimeError('%d already set %s' % (code, op_codes[code]))
    op_codes[code] = op


def run_2(input):
    examples, program = parse(input)

    op_codes = {}
    while len(op_codes) < len(OPS):
        found = False
        remaining = [op for op in OPS if op not in op_codes.values()]
        code_to_op = defaultdict(lambda: set())
        op_to_code = defaultdict(lambda: set())

        for ex in examples:
            code = ex[1][0]
            if code in op_codes.keys():
                continue

            for op in remaining:
                if check_op(ex, op):
                    code_to_op[code].add(op)
                    op_to_code[op].add(code)

        for k, v in code_to_op.items():
            if len(v) == 1:
                check_and_add(op_codes, k, list(v)[0])
                found = True
        for k, v in op_to_code.items():
            if len(v) == 1:
                check_and_add(op_codes, list(v)[0], k)
                found = True

        if not found:
            raise RuntimeError('Nothing new found')

    regs = [0, 0, 0, 0]
    for l in program:
        exec(op_codes, regs, l)
    return regs[0]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])
