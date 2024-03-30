
def read_input(filename: str):
    with open(filename, 'r') as f:
        return f.readline()


# Part 1

FILE = 'day3.txt'
instructions = read_input(FILE)
curr_pos = (0, 0)
visited = set([curr_pos])

MOVES = { '^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0) }

for instruction in instructions:
    i, j = curr_pos
    vx, vy = MOVES[instruction]
    curr_pos = (i + vx, j + vy)
    visited.add(curr_pos)
print(len(visited))


# Part 2

santa_pos = (0, 0)
robosanta_pos = (0, 0)
visited = set([santa_pos, robosanta_pos])

for n in range(0, len(instructions), 2):
    i, j = santa_pos
    vx, vy = MOVES[instructions[n]]
    santa_pos = (i + vx, j + vy)
    visited.add(santa_pos)

    i, j = robosanta_pos
    vx, vy = MOVES[instructions[n+1]]
    robosanta_pos = (i + vx, j + vy)
    visited.add(robosanta_pos)

print(len(visited))
