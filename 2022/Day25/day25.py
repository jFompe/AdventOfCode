from typing import List


def snafu_to_decimal(snafu: str) -> int:
    decimal = 0
    for i,c in enumerate(snafu[::-1]):
        base = 5 ** i
        if c in ('0', '1', '2'):
            decimal += base * int(c)
        elif c == '-':
            decimal -= base
        else:
            decimal -= 2 * base
    return decimal

REMAIDER_TO_SYMBOL = { 0: '0', 1: '1', 2: '2', 3: '=', 4: '-', 5: '0' }

def decimal_to_snafu(decimal: int) -> str:
    snafu = ''
    acc = 0
    while decimal:
        decimal, remainder = decimal // 5, decimal % 5
        remainder += acc
        next = REMAIDER_TO_SYMBOL[remainder]
        snafu = next + snafu
        acc = remainder in (3,4,5)
    return snafu


def read_input(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]


# Part 1

FILE = 'day25.txt'
snafu_numbers = read_input(FILE)
decimal_numbers = [snafu_to_decimal(s) for s in snafu_numbers]
total = sum(decimal_numbers)
snafu_total = decimal_to_snafu(total)
print(snafu_total)
