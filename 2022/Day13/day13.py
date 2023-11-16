from typing import List
from functools import cmp_to_key


def compare_pair(left, right):

    if len(left) < len(right):
        left += [None] * (len(right) - len(left))
    if len(right) < len(left):
        right += [None] * (len(left) - len(right))

    for l, r in zip(left, right):
        if l is None:
            return True
        if r is None:
            return False
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            if l > r:
                return False
            res = None
        elif isinstance(l, list) and isinstance(r, list):
            res = compare_pair(l, r)
        else:
            res = compare_pair(l, [r]) if isinstance(l, list) else compare_pair([l], r)
        if res is not None:
            return res
    return None


def read_input(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [eval(l) for l in f.readlines() if l.strip()]


# Part 1

FILE = 'day13.txt'
lines = read_input(FILE)

n = 0
ind = 1
while lines:
    left = lines.pop(0)
    right = lines.pop(0)
    res = compare_pair(left, right)
    n += res * ind
    ind += 1
print(n)


# Part 2

def pair_comparer(left, right):
    return -1 if compare_pair(left, right) else 1

DIV1 = [[2]]
DIV2 = [[6]]
lines = read_input(FILE)
lines.extend((DIV1, DIV2))
lines.sort(key=cmp_to_key(pair_comparer))

idx1 = lines.index(DIV1) + 1
idx2 = lines.index(DIV2) + 1

print(idx1 * idx2)
