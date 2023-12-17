from typing import List


def read_input(filename: str) -> List[List[str]]:
    with open(filename, 'r') as f:
        return [list(l.strip()) for l in f.readlines()]

def tilt_north(rocks: List[List[str]]):
    for i, row in enumerate(rocks[1:], 1):
        for j, rock in enumerate(row):
            if rock != 'O' or rocks[i-1][j] in ('O', '#'):
                continue
            i_up = i - 1
            while i_up > 0 and rocks[i_up - 1][j] == '.':
                i_up -= 1
            rocks[i_up][j] = 'O'
            rocks[i][j] = '.'

def calculate_load(rocks: List[List[str]]) -> int:
    load = 0
    for i, row in enumerate(rocks):
        for rock in row:
            if rock == 'O':
                load += len(rocks) - i 
    return load


# Part 1

FILE = 'day14.txt'
rocks = read_input(FILE)
tilt_north(rocks)
print(calculate_load(rocks))


# Part 2

def tilt_west(rocks: List[List[str]]) -> None:
    for i, row in enumerate(rocks):
        for j, rock in enumerate(row[1:], 1):
            if rock != 'O' or row[j-1] in ('O', '#'):
                continue
            j_left = j - 1
            while j_left > 0 and row[j_left - 1] == '.':
                j_left -= 1
            rocks[i][j_left] = 'O'
            rocks[i][j] = '.'

def tilt_south(rocks: List[List[str]]) -> None:
    tilt_north(rocks[::-1])

def tilt_east(rocks: List[List[str]]) -> None:
    for i, row in enumerate(rocks):
        for j in range(len(row)-2, -1, -1):
            if row[j] != 'O' or row[j+1] in ('O', '#'):
                continue
            j_right = j + 1
            while j_right < len(row)-1 and row[j_right + 1] == '.':
                j_right += 1
            rocks[i][j_right] = 'O'
            rocks[i][j] = '.'


for i in range(1000):
    tilt_north(rocks)
    tilt_west(rocks)
    tilt_south(rocks)
    tilt_east(rocks)

print(calculate_load(rocks))
