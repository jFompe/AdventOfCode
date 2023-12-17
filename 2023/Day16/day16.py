from dataclasses import dataclass
from typing import List


@dataclass
class Beam:
    i: int
    j: int
    direction: str


def read_input(filename: str):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]

def calculate_energized_tiles(tiles: List[str], initial_beam: Beam) -> int:
    energized_tiles = [[False for _ in tiles[0]] for _ in tiles]
    beams = [initial_beam]

    while beams:
        current_beam = beams.pop(0)

        if not energized_tiles[current_beam.i][current_beam.j]:
            energized_tiles[current_beam.i][current_beam.j] = True

        current_tile = tiles[current_beam.i][current_beam.j]

        if current_beam.direction == 'R':
            if current_tile == '|':
                if energized_tiles[current_beam.i][current_beam.j] != 2:
                    if current_beam.i - 1 >= 0:
                        beams.append(Beam(current_beam.i-1, current_beam.j, 'U'))
                    if current_beam.i + 1 < len(tiles):
                        beams.append(Beam(current_beam.i+1, current_beam.j, 'D'))
                    energized_tiles[current_beam.i][current_beam.j] = 2
            elif current_tile == '/':
                if current_beam.i - 1 >= 0:
                    beams.append(Beam(current_beam.i-1, current_beam.j, 'U'))
            elif current_tile == '\\':
                if current_beam.i + 1 < len(tiles):
                    beams.append(Beam(current_beam.i+1, current_beam.j, 'D'))
            else:
                if current_beam.j + 1 < len(tiles[0]):
                    beams.append(Beam(current_beam.i, current_beam.j+1, 'R'))

        if current_beam.direction == 'L':
            if current_tile == '|':
                if energized_tiles[current_beam.i][current_beam.j] != 2:
                    if current_beam.i - 1 >= 0:
                        beams.append(Beam(current_beam.i-1, current_beam.j, 'U'))
                    if current_beam.i + 1 < len(tiles):
                        beams.append(Beam(current_beam.i+1, current_beam.j, 'D'))
                    energized_tiles[current_beam.i][current_beam.j] = 2
            elif current_tile == '\\':
                if current_beam.i - 1 >= 0:
                    beams.append(Beam(current_beam.i-1, current_beam.j, 'U'))
            elif current_tile == '/':
                if current_beam.i + 1 < len(tiles):
                    beams.append(Beam(current_beam.i+1, current_beam.j, 'D'))
            else:
                if current_beam.j - 1 >= 0:
                    beams.append(Beam(current_beam.i, current_beam.j-1, 'L'))

        if current_beam.direction == 'U':
            if current_tile == '-':
                if energized_tiles[current_beam.i][current_beam.j] != 2:
                    if current_beam.j - 1 >= 0:
                        beams.append(Beam(current_beam.i, current_beam.j-1, 'L'))
                    if current_beam.j + 1 < len(tiles[0]):
                        beams.append(Beam(current_beam.i, current_beam.j+1, 'R'))
                    energized_tiles[current_beam.i][current_beam.j] = 2
            elif current_tile == '/':
                if current_beam.j + 1 < len(tiles[0]):
                    beams.append(Beam(current_beam.i, current_beam.j+1, 'R'))
            elif current_tile == '\\':
                if current_beam.j - 1 >= 0:
                    beams.append(Beam(current_beam.i, current_beam.j-1, 'L'))
            else:
                if current_beam.i - 1 >= 0:
                    beams.append(Beam(current_beam.i-1, current_beam.j, 'U'))

        if current_beam.direction == 'D':
            if current_tile == '-':
                if energized_tiles[current_beam.i][current_beam.j] != 2:
                    if current_beam.j - 1 >= 0:
                        beams.append(Beam(current_beam.i, current_beam.j-1, 'L'))
                    if current_beam.j + 1 < len(tiles[0]):
                        beams.append(Beam(current_beam.i, current_beam.j+1, 'R'))
                    energized_tiles[current_beam.i][current_beam.j] = 2
            elif current_tile == '/':
                if current_beam.j - 1 >= 0:
                    beams.append(Beam(current_beam.i, current_beam.j-1, 'L'))
            elif current_tile == '\\':
                if current_beam.j + 1 < len(tiles[0]):
                    beams.append(Beam(current_beam.i, current_beam.j+1, 'R'))
            else:
                if current_beam.i + 1 < len(tiles):
                    beams.append(Beam(current_beam.i+1, current_beam.j, 'D'))

    return sum([i > 0 for row in energized_tiles for i in row])


# Part 1

FILE = 'day16.txt'
tiles = read_input(FILE)
print(calculate_energized_tiles(tiles, Beam(0, 0, 'R')))


# Part 2

possible_starting_beams = [Beam(0, j, 'D') for j in range(len(tiles[0]))]
possible_starting_beams += [Beam(i, 0, 'R') for i in range(len(tiles))]
possible_starting_beams += [Beam(i, len(tiles)-1, 'L') for i in range(len(tiles))]
possible_starting_beams += [Beam(len(tiles[0])-1, j, 'U') for j in range(len(tiles[0]))]

print(max([calculate_energized_tiles(tiles, beam) for beam in possible_starting_beams]))
