from collections import Counter


with open('day11.txt', 'r') as f:
    rocks = Counter(int(n) for n in f.readline().strip().split())


def blink(rocks):
    next_rocks = {}
    for rock, amount in rocks.items():
        if rock == 0:
            next_rocks[1] = next_rocks.get(1, 0) + amount
        elif len(str(rock)) % 2 == 0:
            half = len(str(rock)) // 2
            next_rocks[int(str(rock)[:half])] = next_rocks.get(int(str(rock)[:half]), 0) + amount
            next_rocks[int(str(rock)[half:])] = next_rocks.get(int(str(rock)[half:]), 0) + amount
        else:
            next_rocks[rock * 2024] = next_rocks.get(rock * 2024, 0) + amount
    return next_rocks

for i in range(75):
    rocks = blink(rocks)
print(sum(rocks.values()))