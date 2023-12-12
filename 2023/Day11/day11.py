from typing import List, Tuple


def read_input(filename: str):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]


def find_empty_lines(galaxies) -> Tuple[List[int], List[int]]:
    rows = [i for i,l in enumerate(galaxies) if '#' not in l]
    cols = [j for j in range(len(galaxies[0])) if '#' not in [l[j] for l in galaxies]]
    return rows, cols

def find_galaxies(galaxies) -> List[Tuple[int, int]]:
    return [(i,j) for i in range(len(galaxies)) for j in range(len(galaxies[0])) if galaxies[i][j] == '#']

def get_distance(g1, g2, empties, empties_multiplier):
    g1x, g1y = g1
    g2x, g2y = g2
    empty_rows, empty_cols = empties
    
    extra_rows = len([n for n in empty_rows if n > min(g1x, g2x) and n < max(g1x, g2x)])
    extra_cols = len([n for n in empty_cols if n > min(g1y, g2y) and n < max(g1y, g2y)])

    return abs(g1x-g2x) + abs(g1y-g2y) + (extra_rows + extra_cols) * (empties_multiplier - 1)

def get_sum_lengths(galaxy_positions, empties, empties_multiplier):
    sum_lengths = 0
    for i in range(len(galaxy_positions)):
        for j in range(i, len(galaxy_positions)):
            if i != j:
                sum_lengths += get_distance(galaxy_positions[i], galaxy_positions[j], empties, empties_multiplier)
    return sum_lengths


# Part 1

FILE = 'day11.txt'
galaxies = read_input(FILE)

empties = find_empty_lines(galaxies)
galaxy_positions = find_galaxies(galaxies)

print(get_sum_lengths(galaxy_positions, empties, 2))


# Part 2

print(get_sum_lengths(galaxy_positions, empties, 1_000_000))
