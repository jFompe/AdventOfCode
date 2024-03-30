
def read_input(filename: str):
    with open(filename, 'r') as f:
        return f.readline()


# Part 1

FILE = 'day1.txt'
instructions = read_input(FILE)
n_floor = 0
INSTRUCTION_CONVERSION = { '(': 1, ')': -1 }
for instruction in instructions:
    n_floor +=  INSTRUCTION_CONVERSION[instruction]
print(n_floor)


# Part 2

BASEMENT = -1
n_floor = 0
for i, instruction in enumerate(instructions):
    n_floor += INSTRUCTION_CONVERSION[instruction]
    if n_floor == BASEMENT:
        print(i+1)
        exit()
