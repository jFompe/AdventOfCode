

with open('day3.txt', 'r') as f:
    batteries = [list(map(int, tuple(l.strip()))) for l in f.readlines()]

total = 0

for battery in batteries:
    t = max(battery[:-1])
    tid = battery.index(t)
    u = max(battery[tid+1:])
    total += t * 10 + u

print(total)


# Part 2

total = 0

for battery in batteries:
    for i in range(12):
        end = 12 - i - 1
        t = max(battery[:-end] or battery)
        battery = battery[battery.index(t) + 1:]
        total += t * 10 ** end

print(total)
