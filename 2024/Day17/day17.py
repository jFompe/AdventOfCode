import re


with open('day17.txt', 'r') as f:
    reg_A = int(re.findall(r'Register A: (\d+)', f.readline())[0])
    reg_B = int(re.findall(r'Register B: (\d+)', f.readline())[0])
    reg_C = int(re.findall(r'Register C: (\d+)', f.readline())[0])
    f.readline()
    operations = [int(op) for op in f.readline().strip().removeprefix('Program: ').split(',')]

print(reg_A, reg_B, reg_C, operations)


def get_combo(operand):
    if operand in range(0,4):
        return operand
    if operand == 4:
        return reg_A
    if operand == 5:
        return reg_B
    if operand == 6:
        return reg_C
    assert operand != 7


i = 0
output = []
while i < len(operations):
    if operations[i] == 0:
        reg_A = reg_A // (2 ** get_combo(operations[i+1]))
    if operations[i] == 1:
        reg_B = reg_B ^ operations[i+1]
    if operations[i] == 2:
        reg_B = get_combo(operations[i+1]) % 8
    if operations[i] == 3 and reg_A != 0:
        i = operations[i+1]
        continue
    if operations[i] == 4:
        reg_B = reg_B ^ reg_C
    if operations[i] == 5:
        output.append(get_combo(operations[i+1]) % 8)
    if operations[i] == 6:
        reg_B = reg_A // (2 ** get_combo(operations[i+1]))
    if operations[i] == 7:
        reg_C = reg_A // (2 ** get_combo(operations[i+1]))
    i += 2

print(','.join([str(o) for o in output]))