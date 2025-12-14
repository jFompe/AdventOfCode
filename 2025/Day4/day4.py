

with open('day4.txt', 'r') as f:
    grid = [list(row.strip()) for row in f.readlines()]

total = 0

for r, row in enumerate(grid):
    for c, location in enumerate(row):

        if location == '.':
            continue

        rolls = 0
        for i in (-1, 0, 1):
            for j in (-1, 0 , 1):
                if i == 0 and j == 0:
                    continue

                if r + i < 0 or r + i >= len(grid) or c + j < 0 or c + j >= len(grid[0]):
                    continue
                rolls += grid[r + i][c + j] == '@'

        if rolls < 4:
            total += 1

print(total)


# Part 2

total = 0

any_removed = True

while any_removed:
    any_removed = False

    for r, row in enumerate(grid):
        for c, location in enumerate(row):

            if location == '.':
                continue

            rolls = 0
            for i in (-1, 0, 1):
                for j in (-1, 0 , 1):
                    if i == 0 and j == 0:
                        continue

                    if r + i < 0 or r + i >= len(grid) or c + j < 0 or c + j >= len(grid[0]):
                        continue
                    rolls += grid[r + i][c + j] == '@'

            if rolls < 4:
                total += 1
                grid[r][c] = '.'
                any_removed = True

print(total)
