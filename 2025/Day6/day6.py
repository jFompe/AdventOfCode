from functools import reduce


with open('day6.txt', 'r') as f:
    lines = [l.split() for l in f.readlines()]
    nums = [tuple(map(int, nums)) for nums in lines[:-1]]
    ops = lines[-1]

mult = lambda x, y : x * y
add = lambda x, y : x + y

total = 0
for i, op in enumerate(ops):
    operation = mult if op == '*' else add
    total += reduce(operation, [n[i] for n in nums])

print(total)


# Part 2

with open('day6.txt', 'r') as f:
    lines = [l for l in f.readlines()]
    nums = lines[:-1]
    ops = lines[-1].split()

tnums = [''.join([nums[j][i] for j in range(len(nums))]).strip() for i in range(len(nums[0]))]


total = 0
finished = False
num_op = 0
while True:
    operands = []
    if not tnums or not any(tnums):
        break
    while tnums and (n := tnums.pop(0)):
        operands.append(int(n))

    operation = mult if ops[num_op] == '*' else add
    total += reduce(operation, operands)
    num_op += 1

print(total)
