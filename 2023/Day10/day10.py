from typing import List, Tuple


def read_input(filename: str) -> List[List[str]]:
    with open(filename, 'r') as f:
        return [list(l.strip()) for l in f.readlines()]
    

possible_connections = {'T': ('7', 'F', '|'), 
                        'B': ('J', 'L', '|'), 
                        'L': ('F', 'L', '-'), 
                        'R': ('J', '7', '-') }

pipe_directions = {'|': ('T', 'B'),
                   '-': ('L', 'R'),
                   '7': ('L', 'B'),
                   'L': ('T', 'R'),
                   'F': ('R', 'B'),
                   'J': ('T', 'L') }

opposite_directions = {'T': 'B',
                       'B': 'T',
                       'L': 'R',
                       'R': 'L' }


def check_pipe_by_position(p, pos):
    return p in possible_connections[pos]


def is_pipe_connected(p1, p2, pos):
    if p2 == '.':
        return False
    if p2 == 'S':
        return True
    if p1 == 'S':
        return any(check_pipe_by_position(p2, pos) for pos in possible_connections)
    return any(p == pos and check_pipe_by_position(p2, p) for p in pipe_directions[p1])

def count_pipe_connections(pipes, i, j) -> int:
    if pipes[i][j] == 'S':
        return 2
    if pipes[i][j] == '.':
        return 0
    connections = 0
    if i > 0:
        connections += is_pipe_connected(pipes[i][j], pipes[i-1][j], 'T')
    if i < len(pipes)-1:
        connections += is_pipe_connected(pipes[i][j], pipes[i+1][j], 'B')
    if j > 0:
        connections += is_pipe_connected(pipes[i][j], pipes[i][j-1], 'L')
    if j < len(pipes[0])-1:
        connections += is_pipe_connected(pipes[i][j], pipes[i][j+1], 'R')
    return connections

def find_next_pipe(pipes: List[List[str]], i: int, j: int, direction: str = None) -> Tuple[int, int, str]:
    if not direction:
        if pipes[i-1][j] in possible_connections['T']:
            return i-1, j, 'T'
        if pipes[i+1][j] in possible_connections['B']:
            return i+1, j, 'B'
        if pipes[i][j-1] in possible_connections['L']:
            return i, j-1, 'L'
        if pipes[i][j+1] in possible_connections['R']:
            return i, j+1, 'R'
    
    curr_pipe = pipes[i][j]
    next_dir = next(d for d in pipe_directions[curr_pipe] if d != opposite_directions[direction])
    if next_dir == 'T':
        return i-1, j, next_dir
    if next_dir == 'B':
        return i+1, j, next_dir
    if next_dir == 'L':
        return i, j-1, next_dir
    if next_dir == 'R':
        return i, j+1, next_dir
    return None


def find_loop_steps(pipes):
    steps = 0
    path_points = []
    i,j = next(((i,j) for i in range(len(pipes)) for j in range(len(pipes[0])) if pipes[i][j] == 'S'))
    path_points.append((i,j))
    i,j,d = find_next_pipe(pipes, i, j)
    path_points.append((i,j))
    steps += 1
    while pipes[i][j] != 'S':
        i,j,d = find_next_pipe(pipes, i, j, d)
        path_points.append((i,j))
        steps += 1
    return steps // 2, path_points


# Part 1

FILE = 'day10.txt'
pipes = read_input(FILE)
steps, path = find_loop_steps(pipes)
print(steps)


# Part 2

def clear_pipes_not_in_path(pipes, path):
    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
            if (i,j) not in path:
                pipes[i][j] = '.'

clear_pipes_not_in_path(pipes, path)


pipes2 = [['.' for _ in range(len(pipes[0])*3)] for _ in range(len(pipes)*3)]

for i in range(len(pipes)):
    for j in range(len(pipes[0])):
        pipe = pipes[i][j]
        if pipe == '-':
            pipes2[3*i+1][3*j] = '-'
            pipes2[3*i+1][3*j+1] = '-'
            pipes2[3*i+1][3*j+2] = '-'
        if pipe == '|':
            pipes2[3*i][3*j+1] = '|'
            pipes2[3*i+1][3*j+1] = '|'
            pipes2[3*i+2][3*j+1] = '|'
        if pipe == 'F' or pipe == 'S':
            pipes2[3*i+1][3*j+2] = '-'
            pipes2[3*i+1][3*j+1] = 'F'
            pipes2[3*i+2][3*j+1] = '|'
        if pipe == 'L':
            pipes2[3*i][3*j+1] = '|'
            pipes2[3*i+1][3*j+1] = 'L'
            pipes2[3*i+1][3*j+2] = '-'
        if pipe == '7':
            pipes2[3*i+1][3*j] = '-'
            pipes2[3*i+1][3*j+1] = '7'
            pipes2[3*i+2][3*j+1] = '|'
        if pipe == 'J':
            pipes2[3*i][3*j+1] = '|'
            pipes2[3*i+1][3*j+1] = 'J'
            pipes2[3*i+1][3*j] = '-'

total = 0
for i in range(len(pipes)):
    crossed = 0
    for j in range(len(pipes[0])):
        if pipes2[3*i][3*j+1] == '|':
            crossed += 1
            continue
        if pipes2[3*i+1][3*j+1] == '.' and crossed % 2 == 1:
            pipes2[3*i][3*j+1] = 'X'
            total += 1
print(total)