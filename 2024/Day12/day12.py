from pprint import pprint
from typing import List


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

    @property
    def area(self):
        return 1

    @property
    def perimeter(self):
        return 4 - sum([n.value == self.value for n in self.neighbours])

    def __str__(self):
        # return f'[{self.value}] - ' + '|'.join([n.value for n in self.neighbours])
        return str(self.region)[-1]

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



