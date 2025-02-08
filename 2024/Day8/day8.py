
with open('day8.txt', 'r') as f:
    grid = [l.strip() for l in f.readlines()]

print(grid)

antennas = {}
for r in range(len(grid)):
    for c in range(len(grid[0])):
        antenna = grid[r][c]
        if antenna == '.':
            continue

        if antenna not in antennas:
            antennas[antenna] = []
        antennas[antenna].append((r,c))
print(antennas)


locations = set()
for antenna_type, positions in antennas.items():
    for i in range(0, len(positions) - 1):
        for j in range(i + 1, len(positions)):
            a1,a2 = min(positions[i], positions[j], key=lambda x:x[0])
            b1,b2 = max(positions[i], positions[j], key=lambda x:x[0])
            d1 = b1 - a1
            d2 = b2 - a2
            x1,x2 = a1 - d1, a2 - d2
            y1,y2 = b1 + d1, b2 + d2
            if 0 <= x1 < len(grid) and 0 <= x2 < len(grid):
                locations.add((x1,x2))
            if 0 <= y1 < len(grid[0]) and 0 <= y2 < len(grid[0]):
                locations.add((y1,y2))
print(len(locations))
