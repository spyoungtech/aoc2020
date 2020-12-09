from more_itertools import windowed
from itertools import combinations
def parse(file='input.txt'):
    with open(file) as f:
        lines = [int(l) for l in f.readlines() if l]
    return lines


def main():
    for window in windowed(parse(), 26):
        previous = window[:-1]
        num = window[-1]
        sums = set()
        for combo in combinations(previous, 2):
            s = sum(combo)
            sums.add(s)
        if num not in sums:
            return num

def part2():
    m = main()
    lines = parse()

    for i in range(2, len(lines)):
        for window in windowed(lines, i):
            if sum(window) == m:
                print(min(window) + max(window))
                return window

if __name__ == '__main__':
    print(main())
    print(part2())