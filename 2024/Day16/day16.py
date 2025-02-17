from dataclasses import dataclass
from typing import List, Set


@dataclass
class Coord:
    x: int
    y: int

    @property
    def right(self):
        return Coord(self.x, self.y + 1)

    @property
    def left(self):
        return Coord(self.x, self.y - 1)

    @property
    def up(self):
        return Coord(self.x - 1, self.y)

    @property
    def down(self):
        return Coord(self.x + 1, self.y)

@dataclass
class Move:
    coord: Coord
    value: str
    dir: str
    score: int

    def __hash__(self):
        return self.coord.x * 1000 + self.coord.y

def find_pos(map, pos):
    for i, row in enumerate(map):
        for j, val in enumerate(row):
            if val == pos:
                return Coord(i, j)

def get_neighbours(map, pos: Coord, dir: str) -> List[Move]:
    neighbours = []
    if dir != 'v' and (next_val := map[pos.up.x][pos.up.y]) != '#':
        neighbours.append(Move(pos.up, next_val, '^', 1 if dir == '^' else 1000))
    if dir != '^' and (next_val := map[pos.down.x][pos.down.y]) != '#':
        neighbours.append(Move(pos.down, next_val, 'v', 1 if dir == 'v' else 1000))
    if dir != '<' and (next_val := map[pos.right.x][pos.right.y]) != '#':
        neighbours.append(Move(pos.right, next_val, '>', 1 if dir == '>' else 1000))
    if dir != '>' and (next_val := map[pos.left.x][pos.left.y]) != '#':
        neighbours.append(Move(pos.left, next_val, '<', 1 if dir == '<' else 1000))
    return neighbours


with open('day16.txt', 'r') as f:
    map = [line.strip() for line in f.readlines()]

for l in map:
    print(l)

s = find_pos(map, 'S')
e = find_pos(map, 'E')
print(s, e)



def find_shortest(curr: Coord, dir: str, score: int, visited: Set) -> int:
    neighbours = get_neighbours(map, curr, dir)
    if not neighbours:
        return float('inf')
    for n in neighbours:
        if n.value == 'E':
            return score + n.score

    return min([find_shortest(n.coord, n.dir, score + n.score, (visited | set([n])).copy()) for n in neighbours if n not in visited], default=float('inf'))


print(find_shortest(s, '>', 0, set()))