from re import findall
from typing import List, Tuple
from functools import reduce
from math import sqrt, ceil, floor


def read_input(filename: str) -> Tuple[List[int]]:
    with open(filename, 'r') as f:
        return [int(t) for t in findall(r'(\d+)', f.readline())], [int(d) for d in findall(r'(\d+)', f.readline())]

def find_ways_to_win(time, distance) -> int:
    reachable_distance = lambda hold: hold * (time - hold)
    return sum([reachable_distance(t) > distance for t in range(time)])


# Part 1

FILE = 'day6.txt'
times, distances = read_input(FILE)
ways_to_win = [find_ways_to_win(time, distance) for time, distance in zip(times, distances)]
result = reduce(lambda n, acc : n * acc, ways_to_win, 1)
print(result)


# Part 2

time = int(''.join(map(str, times)))
distance = int(''.join(map(str, distances)))
# print(find_ways_to_win(time, distance))


# Quadratic Equation optimization

# Valid solutions are in the range ceil(r1)-floor(r2)
# where r1,r2 are the solutions of   distance = hold * (time - hold)
# which is equivalent to - (hold^2) + time*hold - distance = 0

def ways_to_win_quadratic_eq(time, distance) -> int:
    a = -1
    b = time
    c = -distance
    r1 = (- b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    r2 = (- b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    return floor(max(r1,r2)) - ceil(min(r1,r2)) + 1

print(ways_to_win_quadratic_eq(time, distance))
