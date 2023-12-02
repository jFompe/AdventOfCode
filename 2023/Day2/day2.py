from re import findall
from functools import reduce


REDS = 12
GREENS = 13
BLUES = 14

def read_input(filename: str):
    total = 0
    with open(filename, 'r') as f:
        for i,l in enumerate(f.readlines()):
            reds_ok = all([n <= REDS for n in map(int, findall(r'(\d+) red', l))])
            greens_ok = all([n <= GREENS for n in map(int, findall(r'(\d+) green', l))])
            blues_ok = all([n <= BLUES for n in map(int, findall(r'(\d+) blue', l))])
            total += (reds_ok and greens_ok and blues_ok) * (i + 1) 
    return total


# Part 1

FILE = 'day2.txt'
print(read_input(FILE))


# Part 2

def read_input_part2(filename: str):
    total = 0
    with open(filename, 'r') as f:
        for l in f.readlines():
            max_red = max(map(int, findall(r'(\d+) red', l)))
            max_green = max(map(int, findall(r'(\d+) green', l)))
            max_blue = max(map(int, findall(r'(\d+) blue', l)))
            total += max_red * max_green * max_blue
    return total

def read_input_part2_oneliner(filename: str):
    with open(filename, 'r') as f:
        return sum([reduce(lambda x,y: x*y, [max(map(int, findall(r'(\d+) ' + color, l))) for color in ('red', 'green', 'blue')]) for l in f.readlines()])

print(read_input_part2(FILE))
print(read_input_part2_oneliner(FILE))
