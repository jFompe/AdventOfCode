from re import findall
from typing import List, Tuple
from functools import reduce


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
print(find_ways_to_win(time, distance))
# TODO Could be optimized using the quadratic ecuation
