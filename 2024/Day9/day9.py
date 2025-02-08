from dataclasses import dataclass
from collections import namedtuple


with open('day9.txt', 'r') as f:
    disk = [int(n) for n in f.readline()]


blocks = []
for i, n in enumerate(disk):
    if i % 2 == 0:
        blocks += [str(i // 2)] * n
    else:
        blocks += ['.'] * n

front = 0
back = len(blocks) - 1
total = 0
while front <= back:
    if blocks[front] == '.':
        while blocks[back] == '.':
            back -= 1
        total += front * int(blocks[back])
        back -= 1
    else:
        total += front * int(blocks[front])
    front += 1

print(total)


# Part 2

@dataclass
class Block:
    start: int
    size: int
    value: str

    def checksum(self):
        return sum((self.start+i)*int(self.value) for i in range(self.size))


blocks2 = []
i = 0
while i < len(blocks):
    st = i
    v = blocks[i]
    size = 1
    i += 1
    while i < len(blocks) and blocks[i] == v:
        size += 1
        i += 1

    if size:
        blocks2.append(Block(st, size, v))


not_empty_blocks = [block for block in blocks2 if block.value != '.']
empty_blocks = [block for block in blocks2 if block.value == '.']

total = 0
while not_empty_blocks:
    block = not_empty_blocks.pop(-1)
    filled = False

    for empty_block in empty_blocks:
        if empty_block.start > block.start:
            break

        if empty_block.size >= block.size:
            block.start = empty_block.start
            filled = True

        if empty_block.size > block.size:
            empty_block.start += block.size
            empty_block.size -= block.size
            break
        elif empty_block.size == block.size:
            empty_blocks.remove(empty_block)
            break

    total += block.checksum()

print(total)
