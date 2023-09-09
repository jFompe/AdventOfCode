from typing import List


class Rucksack:
    def __init__(self, content: str) -> None:
        half = len(content) // 2
        self.half1 = content[:half]
        self.half2 = content[half:]

    def find_error_value(self):
        error = ord(self._find_error())
        if error >= 97:
            return error - 96
        return error - 38

    def _find_error(self) -> str:
        return list(set(self.half1).intersection(self.half2))[0]


def read_rucksacks(filename: str) -> List[Rucksack]:
    with open(filename, 'r') as f:
        return [Rucksack(l.strip()) for l in f.readlines()]
    

# Part 1

FILE = 'day3.txt'
rucksacks = read_rucksacks(FILE)
priorities = [r.find_error_value() for r in rucksacks]
total = sum(priorities)
print(total)


# Part 2

class GroupedRucksacks:
    def __init__(self, r1: str, r2: str, r3: str) -> None:
        self.rucksack1 = r1
        self.rucksack2 = r2
        self.rucksack3 = r3

    def _find_common(self) -> str:
        return list(set(self.rucksack1).intersection(self.rucksack2).intersection(self.rucksack3))[0]

    def find_common_value(self) -> int:
        common = ord(self._find_common())
        if common >= 97:
            return common - 96
        return common - 38
    
def read_grouped_rucksacks(filename: str) -> List[GroupedRucksacks]:
    rucksacks = []
    with open(filename, 'r') as f:
        while l1 := f.readline().strip():
            l2 = f.readline().strip()
            l3 = f.readline().strip()
            rucksacks.append(GroupedRucksacks(l1, l2, l3))
    return rucksacks

rucksacks = read_grouped_rucksacks(FILE)
priorities = [r.find_common_value() for r in rucksacks]
total = sum(priorities)
print(total)