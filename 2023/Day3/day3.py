from re import finditer, match
from typing	import List, Tuple


def read_input(filename: str):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]


def is_symbol_adjacent(schematics: str, line: int, start: int, end: int):
    if line > 0 and not all(match(r'[0-9\.]', c) for c in schematics[line-1][max(0, start-1):min(end+2, len(schematics[0]))]):
        return True
    if line < len(schematics)-1 and not all(match(r'[0-9\.]', c) for c in schematics[line+1][max(0, start-1):min(end+2, len(schematics[0]))]):
        return True
    if start > 0 and schematics[line][start-1] != '.':
        return True
    if end < len(schematics[0])-1 and schematics[line][end+1] != '.':
        return True
    return False


PATTERN = r'(\d+)'
def calculate_parts(schematics: List[str]) -> int:
    total = 0
    for i,l in enumerate(schematics):
        for n in finditer(PATTERN, l):
            if is_symbol_adjacent(schematics, i, n.start(), n.end()-1):
                total += int(n.group())
    return total


# Part 1

FILE = 'day3.txt'
schematics = read_input(FILE)
total = calculate_parts(schematics)
print(total)


# Part 2

def find_gears(schematics: List[str]) -> List[Tuple]:
    return [(i, m.start()) for i,l in enumerate(schematics) for m in finditer(r'\*', l)]

def find_nums(schematics: List[str]) -> List[Tuple]:
    return [[(*n.span(), int(n.group())) for n in finditer(r'(\d+)', l)] for l in schematics]

def calculate_gear_ratios(schematics: List[str]) -> int:
    nums = find_nums(schematics)
    gears = find_gears(schematics)
    total = 0

    for (row, col) in gears:
        up = nums[row-1] if row-1 >= 0 else None
        mid = nums[row]
        down = nums[row+1] if row+1 < len(nums) else None
        
        nearby_up = list(filter(lambda x: col in range(x[0]-1, x[1]+1), up))
        nearby_mid = list(filter(lambda x: x[1] == col or x[0] == col+1, mid))
        nearby_down = list(filter(lambda x: col in range(x[0]-1, x[1]+1), down))
        adjacents = nearby_up + nearby_mid + nearby_down

        if len(adjacents) == 2:
            total += adjacents[0][2] * adjacents[1][2]
    return total

total = calculate_gear_ratios(schematics)
print(total)
