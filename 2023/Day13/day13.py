from pprint import pprint
from typing import List


def read_input(filename: str) -> List[List[str]]:
    blocks = []
    block = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            l = l.strip()
            if not l:
                blocks.append(block)
                block = []
            else:
                block.append(l)
        blocks.append(block)
    return blocks


def find_reflection_column(block: List[str], old_reflected_col: int = -1) -> int:
    reflection_columns = [i for i in range(1, len(block[0])) if i != old_reflected_col]
    for row in block:
        reflection_columns = [c for c in reflection_columns if row[max(0, 2*c-len(row)):c] == row[c:min(len(row), 2*c)][::-1]]
    if len(reflection_columns) == 1:
        return reflection_columns[0]
    return -1


def find_reflection_row(block: List[str], old_score) -> int:
    transposed_block = [''.join([row[i] for row in block]) for i in range(len(block[0]))]
    return find_reflection_column(transposed_block, old_score)

def calculate_block(block: List[str], old_score: int = -1) -> int:
    ref_col = find_reflection_column(block, old_score if old_score % 100 != 0 else -1)
    if ref_col != -1:
        return ref_col
    return find_reflection_row(block, old_score / 100 if old_score % 100 == 0 else -1) * 100


def calculate_blocks(blocks: List[List[str]]) -> int:
    return sum(map(calculate_block, blocks))


# Part 1

FILE = 'day13.txt'
blocks = read_input(FILE)

print(calculate_blocks(blocks))


# Part 2

def swap_char_at(string: str, at: int):
    swapped = { '.': '#', '#': '.' }
    return string[:at] + swapped[string[at]] + string[at+1:]

def find_new_score(block: List[str]) -> int:
    original_score = calculate_block(block)
    for i, row in enumerate(block):
        for j in range(len(block[0])):
            block[i] = swap_char_at(row, j)
            new_score = calculate_block(block, original_score)
            if new_score > 0 and new_score != original_score:
                return new_score
        block[i] = row
    return -1

print(sum(map(find_new_score, blocks)))
