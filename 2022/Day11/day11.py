
from typing import List
from functools import reduce


class Monkey:
    def __init__(self, st: List[int], op, test: int, y: int, n: int) -> None:
        self.items = st
        self.operation = op
        self.test = test
        self.if_true = y
        self.if_false = n
        self.inspected = 0

    def inspect_items(self, worry_divider: int):
        while self.items:
            it = self.items.pop()
            new = self.do_operation(it)
            new = self.do_inspect(new, worry_divider)
            test = self.do_test(new)
            yield new, self.if_true if test else self.if_false

    def do_inspect(self, item: int, worry_divider=None) -> int:
        self.inspected += 1
        if not worry_divider:
            return item // 3
        else: 
            return item % worry_divider

    def do_operation(self, old: int) -> None:
        return self.operation(old)

    def do_test(self, new) -> bool:
        return new % self.test == 0

    def give_to(self, item: int, other) -> None:
        other.items.append(item)

    def __repr__(self) -> str:
        return f'[{self.starting_items}] {self.operation} {self.test} {self.if_true} {self.if_false}'

class MonkeyManager:
    def __init__(self, monkeys, turns: int, part: int) -> None:
        self.monkeys = monkeys
        self.turns = turns
        self.worry_divider = None if part == 1 else self.get_worry_divider()

    def get_worry_divider(self):
        return reduce(lambda a,b : a*b, [m.test for m in self.monkeys])

    def do_rounds(self):
        for _ in range(self.turns):
            self.do_round()
        a, b, *_ = sorted([monkey.inspected for monkey in self.monkeys], reverse=True)
        return a * b

    def do_round(self):
        for monkey in self.monkeys:
            for (new, next_monkey) in monkey.inspect_items(self.worry_divider):
                monkey.give_to(new, self.monkeys[next_monkey])

def read_items(line: str) -> List[int]:
    line = line.removeprefix('Starting items: ')
    return [int(it) for it in line.split(', ')]

def read_op(line: str):
    line = line.removeprefix('Operation: new = ')
    _, op, b = line.split(' ')
    if op == '*':
        if b == 'old':
            return lambda x: x * x
        return lambda x: x * int(b)
    else:
        return lambda x: x + int(b)

def read_test(line: str) -> int:
    line = line.removeprefix('Test: divisible by ')
    return int(line)

def read_if_true(line: str) -> int:
    line = line.removeprefix('If true: throw to monkey ')
    return int(line)

def read_if_false(line: str) -> int:
    line = line.removeprefix('If false: throw to monkey ')
    return int(line)

def read_monkeys(filename: str) -> List[Monkey]:
    monkeys = []
    with open(filename, 'r') as f:
        while 'Monkey ' in f.readline():
            items = read_items(f.readline().strip())
            op = read_op(f.readline().strip())
            test = read_test(f.readline().strip())
            y = read_if_true(f.readline().strip())
            n = read_if_false(f.readline().strip())
            f.readline()
            monkeys.append(Monkey(items, op, test, y, n))    
    return monkeys


# Part 1

FILE = 'day11.txt'

monkeys = read_monkeys(FILE)
monkey_manager = MonkeyManager(monkeys, 20, 1)
inspections = monkey_manager.do_rounds()
print(inspections)


# Part 2

monkeys = read_monkeys(FILE)
monkey_manager = MonkeyManager(monkeys, 10000, 2)
inspections = monkey_manager.do_rounds()
print(inspections)
