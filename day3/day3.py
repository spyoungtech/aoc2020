from typing import Union
from itertools import cycle, takewhile, dropwhile, repeat
from collections import namedtuple
import math

Slope = namedtuple('Slope', field_names=['right', 'down'])
TREE = "#"


class CyclicalString:
    def __init__(self, s):
        self._initial_string = s

    def __getitem__(self, item: Union[int, slice]) -> str:
        if isinstance(item, slice):
            if item.stop is None:
                raise ValueError("Cannot slice without stop")
            iterable = enumerate(cycle(self._initial_string))
            if item.start:
                iterable = dropwhile(lambda x: x[0] < item.start, iterable)
            return ''.join(
                char for _, char in takewhile(lambda x: x[0] < item.stop, iterable)
            )

        for index, char in enumerate(cycle(self._initial_string)):
            if index == item:
                return char

    def __repr__(self):
        return f'<CyclicalString {repr(self._initial_string)}>'

    def __str__(self):
        return self._initial_string

    def __len__(self):
        return len(self._initial_string)

    def __iter__(self):
        return cycle(self._initial_string)


class Map:
    def __init__(self, rows):
        self.rows = [CyclicalString(row) for row in rows]

    @classmethod
    def from_input(cls, file='input.txt', **kwargs):
        with open(file) as f:
            return cls([line.strip() for line in f if line.strip()], **kwargs)

    def traverse(self, slope: Slope):
        row = 0
        col = 0
        yield self.rows[row][col]
        while True:
            row += slope.down
            col += slope.right
            if row >= len(self.rows):
                break
            yield self.rows[row][col]


def main(right, down):
    map = Map.from_input()
    slope = Slope(right=right, down=down)
    return list(map.traverse(slope)).count(TREE)


if __name__ == '__main__':
    # part 1
    print(main(right=3, down=1))
    # part 2
    print(
        math.prod(
            [
                main(right=1, down=1),
                main(right=3, down=1),
                main(right=5, down=1),
                main(right=7, down=1),
                main(right=1, down=2),
            ]
        )
    )
