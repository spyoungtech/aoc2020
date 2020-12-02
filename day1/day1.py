import itertools
import operator


def load():
    with open('input.txt') as f:
        numbers = [int(line.strip()) for line in f if line]
    return numbers


def find_entries(numbers, goal, r):
    for combo in itertools.combinations(numbers, r):
        if sum(combo) == goal:
            return combo

def product(numbers):
    i = None
    for i in itertools.accumulate(numbers, operator.mul):
        ...
    return i

def _main(goal, r):
    numbers = load()
    entries = find_entries(numbers, goal=goal, r=r)
    return product(entries)


def part_1():
    return _main(goal=2020, r=2)


def part_2():
    return _main(goal=2020, r=3)

if __name__ == '__main__':
    print(part_1())
    print(part_2())
