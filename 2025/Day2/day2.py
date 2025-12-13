

with open('day2.txt', 'r') as f:
    ranges = [tuple(map(int, rang.split('-'))) for rang in f.readline().strip().split(',')]


total = 0

for st, end in ranges:
    for id in range(st, end+1):
        sid = str(id)

        if len(sid) % 2 != 0:
            continue

        half = len(sid) // 2
        if sid[:half] == sid[half:]:
            total += id

print(total)


## Part 2

total = 0

for st, end in ranges:
    for id in range(st, end + 1):
        sid = str(id)
        nchars = len(sid)

        for div in range(1, nchars):
            if nchars % div != 0:
                continue

            splits = [sid[sp*div:(sp+1)*div] for sp in range(nchars // div)]
            if len(set(splits)) == 1:
                print(id)
                total += id
                break

print(total)

