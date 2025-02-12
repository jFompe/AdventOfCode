

MOVES = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}


with open('day15.txt', 'r') as f:
    warehouse = []
    while True:
        line = f.readline().strip()
        if not line:
            break
        warehouse.append(list(line))
    moves = ''.join(line.strip() for line in f.readlines())

for row in warehouse:
    print(row)
print()
print(moves)


def find_start(warehouse):
    for i, row in enumerate(warehouse):
        for j, col in enumerate(row):
            if col == '@':
                return i, j

r,c = find_start(warehouse)
print(r,c)


for move in moves:
    x, y = MOVES[move]

    # Can't move because it's hitting a wall
    if warehouse[r+x][c+y] == '#':
        continue
    # Moves to adjacent position
    if warehouse[r+x][c+y] == '.':
        warehouse[r][c] = '.'
        r += x
        c += y
        warehouse[r][c] = '@'
        continue

    # Otherwise, hits a wall and moves it if possible
    br, bc = r + x, c + y
    while warehouse[br][bc] == 'O':
        br += x
        bc += y

    if warehouse[br][bc] == '.':
        warehouse[br][bc] = 'O'
        warehouse[r][c] = '.'
        warehouse[r+x][c+y] = '@'
        r += x
        c += y


    print()
    for row in warehouse:
        print(''.join(row))

total = 0
for i, row in enumerate(warehouse):
    for j, col in enumerate(row):
        if col == 'O':
            total += 100 * i + j
print(total)
