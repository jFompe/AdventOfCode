from typing import List


class Instruction:
    def __init__(self, op, arg, cycles) -> None:
        self.op = op
        self.arg = arg
        self.cycles = cycles


class InstructionFactory:
    @staticmethod
    def from_string(inst: str) -> Instruction:
        if inst.startswith('noop'):
            return Instruction('noop', 0, 1)
        if inst.startswith('addx'):
            arg = inst.split(' ')[1]
            return Instruction('addx', int(arg), 2)


class CPU:
    def __init__(self, instructions: List[Instruction]) -> None:
        self.X = 1
        self.clock = 0
        self.instructions = instructions
        self.curr_instruction = None

    def hash_next_cycle(self) -> bool:
        return self.instructions or self.curr_instruction

    def next_cycle(self) -> None:
        self._start_cycle()
        value_during_cycle = self.X
        self._end_cycle()
        return value_during_cycle

    def _start_cycle(self):
        if not self.curr_instruction:
            self.curr_instruction = self.instructions.pop(0)
        self.curr_instruction.cycles -= 1

    def _end_cycle(self):
        if not self.curr_instruction.cycles:
            self._execute_instruction()
        self.clock += 1

    def _execute_instruction(self):
        if self.curr_instruction.op == 'addx':
            self.X += self.curr_instruction.arg
        self.curr_instruction = None


def read_instructions(filename: str) -> List:
    with open(filename, 'r') as f:
        return [InstructionFactory.from_string(l.strip()) for l in f.readlines()]


# Part 1

FILE = 'day10.txt'
instructions = read_instructions(FILE)

relevant_cycles = (20, 60, 100, 140, 180, 220)
cpu = CPU(instructions)

total = 0
while cpu.hash_next_cycle():
    cycle_value = cpu.next_cycle()
    if cpu.clock in relevant_cycles:
        total += cycle_value * cpu.clock
print(total)


# Part 2

instructions = read_instructions(FILE)
cpu = CPU(instructions)
COLS = 40

while cpu.hash_next_cycle():
    cycle_value = cpu.next_cycle()
    print('#' if abs((cpu.clock + -1) % 40 - cycle_value) <= 1 else '.', end='')
    if cpu.clock % COLS == 0:
        print()
