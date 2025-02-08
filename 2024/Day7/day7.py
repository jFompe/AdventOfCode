from re import findall


with open('day7.txt', 'r') as f:
    equations = []
    for l in f.readlines():
        equations.append([int(n) for n in findall(r'\d+', l.strip())])

def can_solve_eq(target, operands):
    if len(operands) == 2:
        a, b = operands
        return a * b == target or a + b == target
    is_reducible_sum = can_solve_eq(target - operands[-1], operands[:-1])
    is_reducible_mult = target % operands[-1] == 0 and can_solve_eq(target // operands[-1], operands[:-1])
    return is_reducible_sum or is_reducible_mult

total = 0
for eq in equations:
    if can_solve_eq(eq[0], eq[1:]):
        total += eq[0]
print(total)


# PART 2

def can_solve_eq(target, operands):
    if len(operands) == 2:
        a, b = operands
        return a * b == target or a + b == target or int(f'{a}{b}') == target
    is_reducible_sum = can_solve_eq(target - operands[-1], operands[:-1])
    is_reducible_mult = target % operands[-1] == 0 and can_solve_eq(target // operands[-1], operands[:-1])
    is_reducible_concat = str(target).endswith(str(operands[-1])) and target > operands[-1] and can_solve_eq(int(str(target).removesuffix(str(operands[-1]))), operands[:-1])
    return is_reducible_sum or is_reducible_mult or is_reducible_concat

total = 0
for eq in equations:
    if can_solve_eq(eq[0], eq[1:]):
        total += eq[0]
print(total)


