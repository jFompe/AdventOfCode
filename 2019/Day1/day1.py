

with open('day1.txt', 'r') as f:
    modules = [int(l.strip()) for l in f.readlines()]

total = 0
for module in modules:
    total += (module // 3) - 2
print(total)


# Part 2

total = 0
for module in modules:
    while module > 0:
        module = (module // 3) - 2
        if module > 0:
            total += module
print(total)
