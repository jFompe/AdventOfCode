from typing import List

class Elf:
    def __init__(self, calories: List[int]) -> None:
        self.calories = calories

    def total(self) -> int:
        return sum(self.calories)

    def __repr__(self) -> str:
        return str(self.calories)


def read_elves_calories(filename: str) -> List[Elf]:
    elves = []
    current_calories = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            l = l.strip()
            if not l:
                elves.append(Elf(current_calories))
                current_calories = []
            else:
                current_calories.append(int(l))
    elves.append(Elf(current_calories))
    return elves


# PART 1

FILE = 'input1.txt'
elves = read_elves_calories(FILE)
total_calories = list(map(lambda x: x.total(), elves))
max_calories = max(total_calories)
print(max_calories)



# PART 2

sorted_calories = sorted(total_calories, reverse=True)
total_top3_calories = sum(sorted_calories[:3])
print(total_top3_calories) 