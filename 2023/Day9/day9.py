from typing import List


def read_input(filename: str) -> List[List[int]]:
    with open(filename, 'r') as f:
        return [list(map(int, l.strip().split(' '))) for l in f.readlines()]


def find_extrapolated_value(values):
    levels = [values]
    while any(l != 0 for l in levels[-1]):
        levels.append([levels[-1][i+1]-levels[-1][i] for i in range(len(levels[-1])-1)])
    acc = 0
    for l in levels[::-1]:
        acc += l[-1]
    return acc


# Part 1

FILE = 'day9.txt'
values = read_input(FILE)
print(sum(map(find_extrapolated_value, values)))


# Part 2

def find_extrapolated_value_backwards(values):
    levels = [values]
    while any(l != 0 for l in levels[-1]):
        levels.append([levels[-1][i+1]-levels[-1][i] for i in range(len(levels[-1])-1)])
    acc = 0
    for l in levels[::-1]:
        acc = l[0] - acc
    return acc

print(sum(map(find_extrapolated_value_backwards, values)))
