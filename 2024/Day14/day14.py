import re


WIDTH = 101
HEIGHT = 103
SECONDS = 100

def calculate_position(px, py, vx, vy, seconds=0):
    row = (vy * seconds + py) % HEIGHT
    col = (vx * seconds + px) % WIDTH
    return row, col

with open('day14.txt', 'r') as f:
    robots = []
    for line in f.readlines():
        px, py, vx, vy  = [int(n) for n in re.findall(r'-?\d+', line)]
        row, col = calculate_position(px, py, vx, vy, SECONDS)
        robots.append((row, col))

    TL = sum(r[0] < HEIGHT // 2 and r[1] < WIDTH // 2 for r in robots)
    TR = sum(r[0] < HEIGHT // 2 and r[1] > WIDTH // 2 for r in robots)
    BL = sum(r[0] > HEIGHT // 2 and r[1] < WIDTH // 2 for r in robots)
    BR = sum(r[0] > HEIGHT // 2 and r[1] > WIDTH // 2 for r in robots)
    print(TL * TR * BL * BR)


# PART 2

with open('sol.txt', 'w') as out:
    for i in range(10000):
        with open('day14.txt', 'r') as f:
            robots = []
            for line in f.readlines():
                px, py, vx, vy  = [int(n) for n in re.findall(r'-?\d+', line)]
                row, col = calculate_position(px, py, vx, vy, seconds=i)
                robots.append((row, col))

            if len(robots) == len(set(robots)):
                out.write(f'{i} ------------- \n')
                image = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

                for row, col in robots:
                    image[row][col] = 'X'

                for row in image:
                    out.write(''.join(row) + '\n')
