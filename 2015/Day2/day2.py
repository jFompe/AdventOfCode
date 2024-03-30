


def read_input(filename: str):
    with open(filename, 'r') as f:
        return [list(map(int, l.strip().split('x'))) for l in f.readlines()]


def calculate_area(l, w, h):
    lw = l * w
    lh = l * h
    wh = w * h
    min_side = min(lw, lh, wh)
    return 2 * lw + 2 * lh + 2 * wh + min_side


# Part 1

FILE = 'day2.txt'
lines = read_input(FILE)
total_area = 0
for l in lines:
    total_area += calculate_area(*l)
print(total_area)


# Part 2

def calculate_ribbon(l, w, h):
    min_half_perimeter = min(l+w, w+h, h+l)
    return l * w * h + min_half_perimeter * 2

total_ribbon = 0
for l in lines:
    total_ribbon += calculate_ribbon(*l)
print(total_ribbon)
