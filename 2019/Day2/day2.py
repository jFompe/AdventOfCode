from typing import List


class IntcodeProcessor:
    def __init__(self, memory: List[int]):
        self.ptr = 0
        self.mem = memory.copy()

    def run(self, arg1: int, arg2: int):
        self.mem[1] = arg1
        self.mem[2] = arg2
        while True:
            opcode = self._next()

            if opcode == 1: # ADD
                arg1, arg2, arg3 = self._next_n(3)
                self.mem[arg3] = self.mem[arg1] + self.mem[arg2]
            elif opcode == 2: # MUL
                arg1, arg2, arg3 = self._next_n(3)
                self.mem[arg3] = self.mem[arg1] * self.mem[arg2]
            elif opcode == 99: # HALT
                return self.mem[0]
            else:
                return -1

    def _next(self) -> int:
        val = self.mem[self.ptr]
        self.ptr += 1
        return val

    def _next_n(self, n) -> tuple:
        return tuple(self._next() for _ in range(n))



with open('day2.txt', 'r') as f:
    program = [int(op) for op in f.readline().split(',')]

pc = IntcodeProcessor(program)
print(pc.run(12, 2))


# Part 2

for noun in range(100):
    for verb in range(100):
        pc = IntcodeProcessor(program)
        if pc.run(noun, verb) == 19690720:
            print(100 * noun + verb)
            exit()
