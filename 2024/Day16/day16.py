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


def find_pos(map, pos):
    for i, row in enumerate(map):
        for j, val in enumerate(row):
            if val == pos:
                return Coord(i, j)


def get_neighbours(pos: Coord, dir: str):
    neighbours = []
    if dir != 'v' and map[pos.up.x][pos.up.y] != '#':
        neighbours.append((pos, pos.up, '^', 1001 if dir != '^' else 1))
    if dir != '^' and map[pos.down.x][pos.down.y] != '#':
        neighbours.append((pos, pos.down, 'v', 1001 if dir != 'v' else 1))
    if dir != '<' and map[pos.right.x][pos.right.y] != '#':
        neighbours.append((pos, pos.right, '>', 1001 if dir != '>' else 1))
    if dir != '>' and map[pos.left.x][pos.left.y] != '#':
        neighbours.append((pos, pos.left, '<', 1001 if dir != '<' else 1))
    return neighbours



with open('day16.txt', 'r') as f:
    map = [line.strip() for line in f.readlines()]

for l in map:
    print(l)

s = find_pos(map, 'S')
e = find_pos(map, 'E')


print()
distances = [[(float('inf'), None)for c in row] for row in map]
distances[s.x][s.y] = (0, '>')


ns = get_neighbours(s, '>')

while ns:
    frm, to, new_dir, score = ns.pop()
    if distances[frm.x][frm.y][0] + score < distances[to.x][to.y][0]:
        distances[to.x][to.y] = (distances[frm.x][frm.y][0] + score, new_dir)
        ns += get_neighbours(to, new_dir)

print(distances[e.x][e.y][0])
