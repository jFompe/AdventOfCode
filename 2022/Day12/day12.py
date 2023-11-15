from typing import List, NamedTuple
from dataclasses import dataclass


class Coordinate(NamedTuple):
    x: int
    y: int


@dataclass
class Position:
    height: int
    distance: int = float('inf')
    coord: Coordinate = None

    def is_visited(self):
        return self.distance != float('inf')


class ElevationMap:
    start: Coordinate
    end: Coordinate
    positions: List[List[Position]]
    rows: int
    cols: int

    def __init__(self, start_value: int, end_value: int, positions: List[List[Position]]):
        self.positions = positions
        self.start = self.get_coords(start_value)
        self.end = self.get_coords(end_value)
        self.rows = len(positions)
        self.cols = len(positions[0])
        self._init_coords(start_value, end_value)

    def __repr__(self) -> str:
        return f'{self.start} -> {self.end}'

    def _init_coords(self, start_value, end_value):
        for i in range(self.rows):
            for j in range(self.cols):
                self.positions[i][j].coord = Coordinate(i, j)
                if self.positions[i][j].height == start_value:
                    self.positions[i][j].height = 0
                elif self.positions[i][j].height == end_value:
                    self.positions[i][j].height = ord('z') - ord('a')


    def get_coords(self, pos_value):
        for i,r in enumerate(self.positions):
            for j,c in enumerate(r):
                if c.height == pos_value:
                    return Coordinate(i, j)

    def _is_in_map(self, coord: Coordinate):
        return coord.x >= 0 and coord.x < self.rows and coord.y >= 0 and coord.y < self.cols

    def _can_be_previous_move(self, coord: Coordinate, curr_height: int):
        return self.positions[coord.x][coord.y].height + 1 >= curr_height and not self.positions[coord.x][coord.y].is_visited()

    def _can_be_next_move(self, coord: Coordinate, curr_height: int):
        return self.positions[coord.x][coord.y].height - 1 <= curr_height and self.positions[coord.x][coord.y].is_visited()

    def get_adjacents(self, pos: Position, next: bool):
        i, j = pos.coord
        candidates = [Coordinate(x,y) for x,y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]]
        candidates = [coord for coord in candidates if self._is_in_map(coord)]
        adjacent_condition = self._can_be_next_move if next else self._can_be_previous_move
        return [self.positions[coord.x][coord.y] for coord in candidates if adjacent_condition(coord, pos.height)]
    
    def compute_distances(self):
        initial_position = self.positions[self.end.x][self.end.y]
        initial_position.distance = 0
        positions_to_inspect = self.get_adjacents(initial_position, next=False)
        while positions_to_inspect:
            curr_pos = positions_to_inspect.pop(0)
            if curr_pos.is_visited():
                continue
            next_positions: List[Position] = self.get_adjacents(curr_pos, next=True)
            curr_pos.distance = min(map(lambda x: x.distance, next_positions)) + 1
            positions_to_inspect.extend(self.get_adjacents(curr_pos, next=False))

    def get_final_distance(self):
        i,j = elevation_map.start
        return self.positions[i][j].distance


def read_input(filename: str) -> List[List[int]]:
    with open(filename, 'r') as f:
        return [list(map(lambda c: Position(ord(c) - ord('a')), list(f.strip()))) for f in f.readlines()]


# Part 1

FILE = 'day12.txt'
START = ord('S') - ord('a')
END = ord('E') - ord('a')

map_input = read_input(FILE)
elevation_map = ElevationMap(START, END, map_input)
elevation_map.compute_distances()
print(elevation_map.get_final_distance())


# Part 2

print(min([pos.distance for row in elevation_map.positions for pos in row if pos.height == 0]))
