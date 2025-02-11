from pprint import pprint
from typing import List, Dict


OPPOSITE_DIR = { '>': '<', '<': '>', '^': 'v', 'v': '^' }

class Move:
    def __init__(self, str_x, str_y, turn_x, turn_y, dir_turn, dir_opposite):
        self.straight = slice(str_x, str_y)
        self.turn1 = slice(turn_x, turn_y)
        self.dir_turn1 = dir_turn
        self.turn2 = slice(-turn_x, -turn_y)
        self.dir_turn2 = OPPOSITE_DIR[dir_turn]
        self.dir_opposite = dir_opposite

    def __repr__(self):
        return MOVES_PER_DIR[self.dir_opposite].dir_opposite

MOVES_PER_DIR: Dict[str, Move] = {
    '>': Move( 0,  1, -1,  0, '^', '<'),
    '<': Move( 0, -1,  1,  0, 'v', '>'),
    'v': Move( 1,  0,  0,  1, '>', '^'),
    '^': Move(-1,  0,  0, -1, '<', 'v')
}

class Node:
    def __init__(self, value, i, j):
        self.value = value
        self.i = i
        self.j = j
        self.neighbours: List[Node] = []
        self.region = None

    def add_neighbour(self, other):
        self._add_neighbour(other)
        other._add_neighbour(self)

    def _add_neighbour(self, other):
        self.neighbours.append(other)

    def define_region(self, region: int):
        self.region = region
        for neighbour in self.neighbours:
            if self.value == neighbour.value and not neighbour.region:
                neighbour.define_region(region)

    def next_neighbour(self, direction: str):
        move = MOVES_PER_DIR[direction]
        if (n := self[move.turn1]) and self.value == n.value:
            return n, move.dir_turn1, 1
        if (n := self[move.straight]) and self.value == n.value:
            return n, direction, 0
        if (n := self[move.turn2]) and self.value == n.value:
            return n, move.dir_turn2, 1
        return self, move.dir_opposite, 2

    def __getitem__(self, item):
        assert isinstance(item, slice)
        for n in self.neighbours:
            if n.i == self.i + item.start and n.j == self.j + item.stop:
                return n
        return None

    @property
    def area(self):
        return 1

    @property
    def perimeter(self):
        return 4 - sum([n.value == self.value for n in self.neighbours])

    def __str__(self):
        # return f'[{self.value}] - ' + '|'.join([n.value for n in self.neighbours])
        # return str(self.region)[-1]
        return f'({self.i},{self.j})'

    def __repr__(self):
        return str(self)


with open('day12.txt', 'r') as f:
    map = [[Node(v, i, j) for j, v in enumerate(row.strip())] for i, row in enumerate(f.readlines())]


for i, row in enumerate(map):
    for j, node in enumerate(row):
        if j+1 < len(row):
            node.add_neighbour(row[j+1])
        if i+1 < len(map):
            node.add_neighbour(map[i+1][j])

curr_region = 1
for row in map:
    for node in row:
        if not node.region:
            node.define_region(curr_region)
            curr_region += 1

regions = {}
for row in map:
    for node in row:
        if not node.region in regions:
            regions[node.region] = []
        regions[node.region].append(node)

total = 0
for region_nodes in regions.values():
    total_area = sum(node.area for node in region_nodes)
    total_perimeter = sum(node.perimeter for node in region_nodes)
    total += total_area * total_perimeter
print(total)


# Part 2

def count_sides(nodes: List[Node]) -> int:
    if len(nodes) in (1, 2):
        return 4

    curr = start = nodes[0]
    curr_dir = '>'
    sides = 1

    while True:
        curr, curr_dir, sides_added = curr.next_neighbour(curr_dir)
        sides += sides_added
        if curr == start:
            if curr_dir == '<':
                sides += 1
            break
    return sides


total = 0
for region, region_nodes in regions.items():
    total_area = sum(node.area for node in region_nodes)
    num_sides = count_sides(region_nodes)
    # print('Checking region:', region, '->', num_sides, 'sides')
    total += total_area * num_sides
print(total)
