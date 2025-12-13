

with open('day1.txt', 'r') as f:
    rotations = [(l[0], int(l[1:])) for l in f.readlines()]
    print(rotations)

position = 50
counter = 0
for dir, num in rotations:
    if dir == 'R':
        position += num
    elif dir == 'L':
        position -= num
    position %= 100
    if position == 0:
        counter += 1

print(counter)


# PART 2

position = 50
counter = 0

for dir, num in rotations:

    # Kinda ashamed of this tbh but it works
    if dir == 'R':
        for _ in range(num):
            position = (position + 1) % 100
            if position == 0:
                counter += 1

    else:
        for _ in range(num):
            position = (position - 1) % 100
            if position == 0:
                counter += 1

print(counter)
