import itertools
import string
import re
import math


def range_split(r):
    lst = list(r)
    middle = lst[len(lst) // 2]
    lower = range(r.start, middle)
    upper = range(middle, r.stop)
    return upper, lower


def parse(file='input.txt'):
    with open(file) as f:
        return [line.strip() for line in f if line.strip()]




def parse_pass(p):
    row_data = p[:7]
    col_data = p[7:]
    lower = range(0, 64)
    upper = range(64, 128)
    row = None
    for datum in row_data:
        if datum == 'F':
            row = lower
        elif datum == 'B':
            row = upper
        upper, lower = range_split(row)
    row = row.start
    left = range(0, 4)
    right = range(4, 8)
    col = None
    for datum in col_data:
        if datum == 'L':
            col = left
        elif datum == 'R':
            col = right
        right, left = range_split(col)
    col = col.start
    return row, col

values = []

for pp in parse():
    row, col = parse_pass(pp)
    values.append(row * 8 + col)
print(max(values))

last_value = None
for value in sorted(values):
    if last_value and value != last_value + 1:
        print(value-1)
    last_value = value

