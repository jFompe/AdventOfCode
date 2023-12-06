from re import findall, sub
from typing import List, Tuple


def read_input(filename: str):
    cards = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            winning, mine = sub(r'Card\s+\d+:', '', l).split('|')
            winning_numbers = findall(r'(\d+)', winning)
            my_numbers = findall(r'(\d+)', mine)
            cards.append((winning_numbers, my_numbers))
    return cards

def calculate_points(cards: List[Tuple]):
    score = lambda w,m : 0 if not (l := len(set(w).intersection(m))) else 2 ** (l-1)
    return sum(map(lambda c: score(c[0], c[1]), cards))


# Part 1

FILE = 'day4.txt'
cards = read_input(FILE)
print(calculate_points(cards))


# Part 2

card_units = [1 for _ in cards]
for i,c in enumerate(cards):
    winning_numbers = len(set(c[0]).intersection(c[1]))
    for j in range(winning_numbers):
        card_units[i+j+1] += card_units[i]
print(sum(card_units))
