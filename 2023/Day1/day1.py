from typing import List
from re import search, match


def read_input(filename: str) -> List[int]:
    with open(filename, 'r') as f:
        nums_per_line = [[c for c in l if match(r'\d', c)] for l in f.readlines()]
        return [int(nums[0] + nums[-1]) for nums in nums_per_line]


# Part 1

FILE = 'day1.txt'
nums = read_input(FILE)
print(sum(nums))


# Part 2

NUMS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
def parse_num(num: str):
    if match(r'\d', num):
        return num
    return str(NUMS[num])

PATTERN_START = r'(\d|one|two|three|four|five|six|seven|eight|nine)\w*$'
PATTERN_END = r'^\w*(\d|one|two|three|four|five|six|seven|eight|nine).*$'
def read_input_part2(filename: str):
    nums = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            start = search(PATTERN_START, l).groups()
            end = search(PATTERN_END, l).groups()
            nums.append(int(parse_num(start[0]) + parse_num(end[0])))
    return nums

nums = read_input_part2(FILE)
print(sum(nums))