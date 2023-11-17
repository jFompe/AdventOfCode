from typing import List, NamedTuple


class Coordinate(NamedTuple):
    x: int
    y: int


def parse_line(line: str) -> List[Coordinate]:
    return [Coordinate(int(c.split(',')[0]),int(c.split(',')[1])) for c in line.split(' -> ')]

def read_input(filename: str) -> List[List[Coordinate]]:
    with open(filename, 'r') as f:
        return [parse_line(l.strip()) for l in f.readlines()]

def generate_cave(paths, rows, cols):
    cave = [[AIR for _ in range(cols)] for _ in range(rows)]
    for path in paths:
        for i in range(len(path) - 1):
            s = path[i]
            e = path[i+1]
            if s.x == e.x:
                for j in range(min(s.y,e.y), max(s.y,e.y)+1):
                    cave[j][s.x] = ROCK
            else:
                for j in range(min(s.x,e.x), max(s.x,e.x)+1):
                    cave[s.y][j] = ROCK
    return cave

# Part 1

FILE = "day14.txt"
paths = read_input(FILE)

min_x = min([c.x for coords in paths for c in coords])
max_x = max([c.x for coords in paths for c in coords])
max_y = max([c.y for coords in paths for c in coords])

SOURCE = Coordinate(500-min_x, 0)
paths = [[Coordinate(c.x-min_x, c.y) for c in path] for path in paths]

rows = max_y + 1
cols = max_x - min_x + 1

ROCK = '#'
AIR = '.'
SAND = 'o'

cave = generate_cave(paths, rows, cols)


def process_sand(cave):
    units = 0
    abyss = False
    while not abyss:
        gx, gy = SOURCE
        falling = True
        while falling:
            if gy+1 > max_y:
                return units
            elif cave[gy+1][gx] == AIR:
                gy += 1
            elif gx-1 < 0:
                return units
            elif cave[gy+1][gx-1] == AIR:
                gy += 1
                gx -= 1
            elif gx+1 > max_x:
                return units
            elif cave[gy+1][gx+1] == AIR:
                gy += 1
                gx += 1
            else:
                falling = False
                cave[gy][gx] = SAND
        units += 1

print(process_sand(cave))


# Part 2

def process_sand2(cave):
    units = 0
    abyss = False
    while not abyss:
        gx, gy = SOURCE
        falling = True
        while falling:
            if gy+1 < rows and cave[gy+1][gx] == AIR:
                gy += 1
            elif gy+1 < rows and gx-1 > 0 and cave[gy+1][gx-1] == AIR:
                gy += 1
                gx -= 1
            elif gy+1 < rows and gx+1 < cols and cave[gy+1][gx+1] == AIR:
                gy += 1
                gx += 1
            else:
                cave[gy][gx] = SAND
                falling = False
                if gx == SOURCE.x and gy == SOURCE.y:
                    return units + 1
        units += 1

rows += 2
cols = cols * 20
SOURCE = Coordinate(SOURCE.x+cols//4, SOURCE.y)
paths = [[Coordinate(c.x+cols//4, c.y) for c in path] for path in paths]
paths.append([Coordinate(0, rows-1), Coordinate(cols-1, rows-1)])
cave = generate_cave(paths, rows, cols)

print(process_sand2(cave))
