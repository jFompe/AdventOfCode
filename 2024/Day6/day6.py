
with open('day6.txt', 'r') as f:
    map = [list(l.strip()) for l in f.readlines()]


def get_starting_pos(map):
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == '^':
                return r,c


r,c = get_starting_pos(map)

exited = False
guard = map[r][c]
while True:

    map[r][c] = 'X'

    if guard == '^':
        nr = r - 1
        nc = c
    elif guard == 'v':
        nr = r + 1
        nc = c
    elif guard == '>':
        nr = r
        nc = c + 1
    elif guard == '<':
        nr = r
        nc = c - 1

    if nr < 0 or nr == len(map) or nc == len(map[0]) or nc < 0:
        break

    if map[nr][nc] == '#':
        if guard == '^':
            guard = '>'
        elif guard == 'v':
            guard = '<'
        elif guard == '>':
            guard = 'v'
        elif guard == '<':
            guard = '^'

    else:
        r = nr
        c = nc

total = 0
for row in map:
    for col in row:
        if col == 'X':
            total += 1
print(total)

for row in map:
    print(''.join(row))