from typing import List


class IntcodeProcessor:
    def __init__(self, memory: List[int]):
        self.ptr = 0
        self.mem = memory.copy()

    def run(self):
        while True:
            opcode, m1, m2, m3 = self._next_instruction()

            if opcode == 1: # ADD
                arg1, arg2, arg3 = self._next_n(3)
                self.mem[arg3] = self._get_param(arg1, m1) + self._get_param(arg2, m2)
            elif opcode == 2: # MUL
                arg1, arg2, arg3 = self._next_n(3)
                self.mem[arg3] = self._get_param(arg1, m1) * self._get_param(arg2, m2)
            elif opcode == 3: # INPUT
                arg1 = self._next()
                self.mem[arg1] = int(input('IN: '))
            elif opcode == 4: # OUTPUT
                arg1 = self._next()
                print('OUT:', self._get_param(arg1, m1))
            elif opcode == 5: # JMP IF TRUE
                arg1, arg2 = self._next_n(2)
                if self._get_param(arg1, m1) != 0:
                    self.ptr = self._get_param(arg2, m2)
            elif opcode == 6: # JMP IF FALSE
                arg1, arg2 = self._next_n(2)
                if self._get_param(arg1, m1) == 0:
                    self.ptr = self._get_param(arg2, m2)
            elif opcode == 7: # LT
                arg1, arg2, arg3 = self._next_n(3)
                self.mem[arg3] = self._get_param(arg1, m1) < self._get_param(arg2, m2)
            elif opcode == 8: # EQ
                arg1, arg2, arg3 = self._next_n(3)
                self.mem[arg3] = self._get_param(arg1, m1) == self._get_param(arg2, m2)
            elif opcode == 99: # HALT
                return self.mem[0]
            else:
                return -1

    def _get_param(self, arg, mode):
        if mode == 0: # POS
            return self.mem[arg]
        if mode == 1: # IMM
            return arg

    def _next_instruction(self):
        instruction = str(self._next())
        opcode = int(instruction[-2:])
        m1 = int(instruction[-3:-2] or 0)
        m2 = int(instruction[-4:-3] or 0)
        m3 = int(instruction[-5:-4] or 0)
        return opcode, m1, m2, m3

    def _next(self) -> int:
        val = self.mem[self.ptr]
        self.ptr += 1
        return val

    def _next_n(self, n) -> tuple:
        return tuple(self._next() for _ in range(n))


with open('day5.txt', 'r') as f:
    program = [int(op) for op in f.readline().split(',')]

pc = IntcodeProcessor(program)
print(pc.run())
