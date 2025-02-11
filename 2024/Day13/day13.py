import re


def solve_equation(ax, ay, bx, by, px, py, max_presses=100):
    a = (by*px - bx*py) / (by*ax - bx*ay)
    b = (ay*px - ax*py) / (ay*bx - ax*by)
    if int(a) != a or int(b) != b:
        return (0, 0)
    if a > max_presses or b > max_presses:
        return (0, 0)
    return (a, b)


with open('day13.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    cost1 = 0
    cost2 = 0
    i = 0
    while i < len(lines):
        button_a = re.findall(r'Button A: X\+(\d+), Y\+(\d+)', lines[i])
        button_b = re.findall(r'Button B: X\+(\d+), Y\+(\d+)', lines[i+1])
        prize = re.findall(r'Prize: X=(\d+), Y=(\d+)', lines[i+2])
        i += 4

        bax, bay = int(button_a[0][0]), int(button_a[0][1])
        bbx, bby = int(button_b[0][0]), int(button_b[0][1])
        px, py = int(prize[0][0]), int(prize[0][1])

        s1, s2 = solve_equation(bax, bay, bbx, bby, px, py)
        cost1 += 3*s1 + s2

        s1, s2 = solve_equation(bax, bay, bbx, bby, px + 10000000000000, py + 10000000000000, max_presses=float('inf'))
        cost2 += 3 * s1 + s2

print(int(cost1))
print(int(cost2))



'''
94a + 22b = 8400 (X)
34a + 67b = 5400 (Y)
cost = 3a + b
a <= 100
b <= 100

a = (8400 - 22b) / 94
b = (8400 - 94a) / 22

a = (5400 - 67b) / 34
b = (5400 - 34a) / 67



(8400 - 22b) / 94 = (5400 - 67b) / 34
(8400 - 94a) / 22 = (5400 - 34a) / 67

34 (8400 - 22b) = 94 (5400 - 67b)
67 (8400 - 94a) = 22 (5400 - 34a)

34*8400 - 34*22b = 94*5400 - 94*67b
67*8400 - 67*94a = 22*5400 - 22*34a

34*8400 - 94*5400 = 34*22b - 94*67b
67*8400 - 22*5400 = 67*94a - 22*34a

34*8400 - 94*5400 = (34*22 - 94*67)b
67*8400 - 22*5400 = (67*94 - 22*34)a

(34*8400 - 94*5400) / (34*22 - 94*67) = b
(67*8400 - 22*5400) / (67*94 - 22*34) = a
'''
