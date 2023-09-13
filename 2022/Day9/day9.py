from typing import List, NamedTuple


class Point:
    def __init__(self) -> None:
        self.x = self.y = 0

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash(self.x + self.y)

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def move(self, dir: str) -> None:
        if 'U' in dir:
            self.y += 1
        elif 'D' in dir:
            self.y -= 1
        if 'R' in dir:
            self.x += 1
        elif 'L' in dir:
            self.x -= 1

    def is_touching(self, other):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def to_tuple(self):
        return (self.x, self.y)
    
    def get_next_move(self, target):
        if self.x == target.x:
            return 'U' if target.y > self.y else 'D'
        if self.y == target.y:
            return 'R' if target.x > self.x else 'L'
        
        mx = 'R' if target.x > self.x else 'L'
        my = 'U' if target.y > self.y else 'D'
        return mx + my


class Step(NamedTuple):
    direction: str
    length: int


def read_steps(filename: str) -> List[Step]:
    with open(filename, 'r') as f:
        return [Step(l[0], int(l.strip()[2:])) for l in f.readlines()]


# Part 1

FILE = 'day9.txt'
steps = read_steps(FILE)
head = Point()
tail = Point()
visited = set([tail.to_tuple()])

for s in steps:
    for _ in range(s.length):
        head.move(s.direction)
        if not tail.is_touching(head):
            next_move = tail.get_next_move(head)
            tail.move(next_move)
            visited.add(tail.to_tuple())
distinct_visited = len(visited)
print(distinct_visited)


# Part 2

rope = [Point() for _ in range(10)]
head = rope[0]
tail = rope[-1]
visited = set([tail.to_tuple()])

for s in steps:
    for _ in range(s.length):
        head.move(s.direction)
        for i in range(1, len(rope)):
            if not rope[i].is_touching(rope[i-1]):
                next_move = rope[i].get_next_move(rope[i-1])
                rope[i].move(next_move)
        visited.add(tail.to_tuple())
distinct_visited = len(visited)
print(distinct_visited)
