from collections import Counter
from functools import cmp_to_key


def read_input(filename: str):
    with open(filename, 'r') as f:
        return [(hand[0], int(hand[1])) for l in f.readlines() if (hand := l.strip().split(' '))]


CARDS_ORDER = 'AKQJT98765432'

def compare_hands(h1, h2):
    if comp := compare_type(h1[0], h2[0]):
        return comp
    return compare_high_cards(h1[0], h2[0])

is_repoker = lambda c: 5 in c.values()
is_poker = lambda c: 4 in c.values()
is_full = lambda c: 3 in c.values() and 2 in c.values()
is_three = lambda c: 3 in c.values()
is_two_pair = lambda c: len([n for n in c.values() if n == 2]) == 2 
is_pair = lambda c: 2 in c.values()
def hand_type_score(h):
    if is_repoker(h):
        return 6
    if is_poker(h):
        return 5
    if is_full(h):
        return 4
    if is_three(h):
        return 3
    if is_two_pair(h):
        return 2
    if is_pair(h):
        return 1
    return 0

def compare_type(h1, h2):
    s1 = hand_type_score(Counter(h1))
    s2 = hand_type_score(Counter(h2))
    if s1 != s2:
        return 1 if s1 > s2 else -1
    return 0

def compare_high_cards(h1, h2):
    def compare_high_card(c1, c2):
        return 1 if CARDS_ORDER.index(c1) < CARDS_ORDER.index(c2) else -1
    for c1, c2 in zip(h1, h2):
        if c1 != c2:
            return compare_high_card(c1, c2)
    return 0

def calculate_winnings(card_hands):
    total = 0
    for i,c in enumerate(card_hands):
        total += (i+1) * c[1]
    return total


# Part 1

FILE = 'day7.txt'
card_hands = read_input(FILE)
card_hands.sort(key=cmp_to_key(compare_hands))
print(calculate_winnings(card_hands))


# Part 2

CARDS_ORDER = 'AKQT98765432J'

def hand_type_score(h):
    if 'J' in h:
        max_c = None
        max_n = -float('inf')
        for c in h:
            if c != 'J' and h[c] > max_n:
                max_c = c
                max_n = h[c]
        h[max_c] += h['J']
        del h['J']

    if is_repoker(h):
        return 6
    if is_poker(h):
        return 5
    if is_full(h):
        return 4
    if is_three(h):
        return 3
    if is_two_pair(h):
        return 2
    if is_pair(h):
        return 1
    return 0

card_hands.sort(key=cmp_to_key(compare_hands))
print(calculate_winnings(card_hands))
