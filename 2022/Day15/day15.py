import re
from typing import NamedTuple, List


class Coordinate(NamedTuple):
    x: int
    y: int

class Sensor(NamedTuple):
    coords: Coordinate
    beacon: Coordinate

    @property
    def distance(self) -> int:
        return manhattan_distance(self.coords, self.beacon)
    
    def get_row_cells_covered(self, row):
        rows_diff = self.coords.y - row
        side_len = self.distance - abs(rows_diff)
        x_from = self.coords.x - side_len
        x_to = self.coords.x + side_len
        return [(x, row) for x in range(x_from, x_to+1)]


INPUT_PATTERN = r'.+x=(-?\d+), y=(-?\d+).+x=(-?\d+), y=(-?\d+)'
def read_input(filename: str) -> List[Sensor]:
    coords = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            sx,sy, bx,by = re.search(INPUT_PATTERN, l).groups()
            coords.append(Sensor(Coordinate(int(sx),int(sy)),Coordinate(int(bx),int(by))))
    return coords


def manhattan_distance(c1: Coordinate, c2: Coordinate):
    return abs(c1.x-c2.x) + abs(c1.y-c2.y)


# Part 1

FILE = 'day15.txt'
positions = read_input(FILE)
TARGET_ROW = 2_000_000

beacons_and_sensors = set([c for s in positions for c in s if c.y == TARGET_ROW])
invalid_positions = set()

for pos in positions:
    if pos.distance > pos.coords.y - TARGET_ROW:
        invalid_positions.update(pos.get_row_cells_covered(TARGET_ROW))
invalid_positions.difference_update(beacons_and_sensors)

print(len(invalid_positions))
