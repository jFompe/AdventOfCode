import re


def read_input(filename: str):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]


def is_nice(input: str) -> bool:
    num_vowesls = lambda s : len(re.findall('[aeiou]', s))
    has_repeated_letter = lambda s: re.match(r'\w*(\w)\1\w*', s) is not None
    contains_forbidden_substr = lambda s : any(subs in s for subs in ('ab', 'cd', 'pq', 'xy'))

    return num_vowesls(input) >= 3 and has_repeated_letter(input) and not contains_forbidden_substr(input)


# Part 1

FILE = 'day5.txt'
lines = read_input(FILE)
nice_strings = 0
for l in lines:
    nice_strings += is_nice(l)
print(nice_strings)


# Part 2

def is_nice2(input: str) -> bool:
    letters_pair_twice = lambda s : re.match(r'\w*(\w\w)\w*\1\w*', s) is not None
    repeated_letter = lambda s : re.match(r'\w*(\w)\w\1\w*', s) is not None
    return letters_pair_twice(input) and repeated_letter(input)


nice_strings = 0
for l in lines:
    nice_strings += is_nice2(l)
print(nice_strings)
