from pprint import pprint


with open('day10.txt', 'r') as f:
    map = [[int(pos) for pos in row.strip()] for row in f.readlines()]


trailheads = []
for i, row in enumerate(map):
    for j, pos in enumerate(row):
        if pos == 0:
            trailheads.append((i,j))


def trailhead_ends(map, i, j, height):
    if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]):
        return []
    if map[i][j] != height:
        return []
    if map[i][j] == 9:
        return [(i,j)]

    ends = set()
    ends.update(trailhead_ends(map, i + 1, j, height + 1))
    ends.update(trailhead_ends(map, i - 1, j, height + 1))
    ends.update(trailhead_ends(map, i, j + 1, height + 1))
    ends.update(trailhead_ends(map, i, j - 1, height + 1))
    return ends

print(sum(len(trailhead_ends(map, i, j, 0)) for i,j in trailheads))


# Part 2

def trailhead_ends(map, i, j, height):
    if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]):
        return []
    if map[i][j] != height:
        return []
    if map[i][j] == 9:
        return [(i,j)]

    ends = list()
    ends.extend(trailhead_ends(map, i + 1, j, height + 1))
    ends.extend(trailhead_ends(map, i - 1, j, height + 1))
    ends.extend(trailhead_ends(map, i, j + 1, height + 1))
    ends.extend(trailhead_ends(map, i, j - 1, height + 1))
    return ends

print(sum(len(trailhead_ends(map, i, j, 0)) for i,j in trailheads))
