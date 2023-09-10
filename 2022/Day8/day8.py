
def is_visible(trees, i, j):
    curr = trees[i][j]
    left = trees[i][:j]
    if max(left) < curr:
        return True
    right = trees[i][j+1:]
    if max(right) < curr:
        return True
    top = [t[j] for t in trees[:i]]
    if max(top) < curr:
        return True
    bottom = [t[j] for t in trees[i+1:]]
    if max(bottom) < curr:
        return True
    return False


# Part 1

FILE = 'day8.txt'
with open(FILE, 'r') as f:
    trees = [[int(t) for t in l.strip()] for l in f.readlines()]
n = len(trees)
m = len(trees[0])

num_visible = n * 2 + (m-2) * 2
for i in range(1,n-1):
    for j in range(1,m-1):
        num_visible += is_visible(trees, i, j)
print(num_visible)


# Part 2

def calculate_line_score(line, val):
    score = 0
    for v in line:
        score += 1
        if v >= val:
            return score
    return score

def calculate_scenic_score(trees, i ,j):
    curr = trees[i][j]
    left = calculate_line_score(trees[i][:j][::-1], curr)
    right = calculate_line_score(trees[i][j+1:], curr)
    top = calculate_line_score([t[j] for t in trees[:i]][::-1], curr)
    bottom = calculate_line_score([t[j] for t in trees[i+1:]], curr)
    return left * right * top * bottom

max_scenic_score = 0
for i in range(1,n-1):
    for j in range(1,m-1):
        scenic_score = calculate_scenic_score(trees, i ,j)
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
print(max_scenic_score)
