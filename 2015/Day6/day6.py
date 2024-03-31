import re


def read_input(filename: str):
    with open(filename, 'r') as f:
        return [re.findall(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', l.strip())[0] for l in f.readlines()]


# Part 1

FILE = 'day6.txt'
lines = read_input(FILE)

SIZE = 1000
lights = [[False for _ in range(SIZE)] for _ in range(SIZE)]

for l in lines:
    action, x1, y1, x2, y2 = l[0], *list(map(int, l[1:]))

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if action == 'turn on':
                lights[i][j] = True
            elif action == 'turn off':
                lights[i][j] = False
            elif action == 'toggle':
                lights[i][j] = not lights[i][j]

print(sum([sum(r) for r in lights]))


# Part 2

SIZE = 1000
lights = [[False for _ in range(SIZE)] for _ in range(SIZE)]

for l in lines:
    action, x1, y1, x2, y2 = l[0], *list(map(int, l[1:]))

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if action == 'turn on':
                lights[i][j] += 1
            elif action == 'turn off':
                lights[i][j] = max(lights[i][j] - 1, 0)
            elif action == 'toggle':
                lights[i][j] += 2

print(sum([sum(r) for r in lights]))
