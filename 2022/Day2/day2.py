from typing import List

ROCK = 1
PAPER = 2
SCISSORS = 3

codes = {
    'A': ROCK,
    'X': ROCK,
    'B': PAPER,
    'Y': PAPER,
    'C': SCISSORS,
    'Z': SCISSORS
}

LOSE = 0
DRAW = 3
WIN = 6


class Round:
    def __init__(self, other: str, mine: str) -> None:
        self.other = other
        self.mine = mine

    def points(self) -> int:
        return codes[self.mine] + self._round_result()
    
    def _round_result(self) -> int:
        if self._is_draw():
            return DRAW
        if self._is_lose():
            return LOSE
        return WIN

    def _is_draw(self) -> bool:
        return codes[self.other] == codes[self.mine]
    
    def _is_lose(self) -> bool:
        is_lose = codes[self.other] == ROCK and codes[self.mine] == SCISSORS
        is_lose = is_lose or codes[self.other] == PAPER and codes[self.mine] == ROCK
        is_lose = is_lose or codes[self.other] == SCISSORS and codes[self.mine] == PAPER
        return is_lose

    def __repr__(self) -> str:
        return f'{self.other} - {self.mine}'
    

def read_rounds(filename: str) -> List[Round]:
    with open(filename, 'r') as f:
        return [Round(l[0], l[2]) for l in f.readlines()]


# PART 1

FILE = 'day2.txt'
rounds = read_rounds(FILE)
results = list(map(lambda x: x.points(), rounds))
total_points = sum(results)
print(total_points)


# PART 2

moves_to_lose = { 'A': 'Z', 'B': 'X', 'C': 'Y' }
moves_to_draw = { 'A': 'X', 'B': 'Y', 'C': 'Z' }
moves_to_win = { 'A': 'Y', 'B': 'Z', 'C': 'X' }
moves = { 'X': moves_to_lose, 'Y': moves_to_draw, 'Z': moves_to_win }


def select_move(other: str, result: str) -> str:
    return moves[result][other]

def read_rounds_deciding_move(filename: str) -> List[Round]:
    with open(filename, 'r') as f:
        return [Round(l[0], select_move(l[0], l[2])) for l in f.readlines()]
    
rounds = read_rounds_deciding_move(FILE)
results = list(map(lambda x: x.points(), rounds))
total_points = sum(results)
print(total_points)