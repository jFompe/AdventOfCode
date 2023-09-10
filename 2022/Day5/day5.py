from typing import List


NUM_STACKS = 9


class Move:
    def __init__(self, line: str) -> None:
        _, amount, _, fromm, _, to = line.split(' ')
        self.amount = int(amount)
        self.fromm = int(fromm)
        self.to = int(to)

    def __repr__(self) -> str:
        return f'move {self.amount} from {self.fromm} to {self.to}'


class Cargo:
    def __init__(self, levels: List[str]) -> None:
        crates = [[] for _ in range(NUM_STACKS)]
        for l in levels[::-1]:
            for i in range(NUM_STACKS):
                if l[i] != ' ':
                    crates[i].append(l[i])
        self.crates = crates

    def __repr__(self) -> str:
        return str(self.crates)

    def process_move(self, move: Move, stacked: bool) -> None:
        if stacked:
            self._process_move_stacked(move)
        else:
            self._process_move_unstacked(move)

    def _process_move_unstacked(self, move: Move) -> None:
        for _ in range(move.amount):
            self.crates[move.to-1].append(self.crates[move.fromm-1].pop())

    def _process_move_stacked(self, move: Move):
        last_n = self.crates[move.fromm-1][-move.amount:]
        del self.crates[move.fromm-1][-move.amount:]
        self.crates[move.to-1].extend(last_n)

    def get_final_state(self):
        return [s[-1] for s in self.crates]


class Ship:
    def __init__(self, cargo: Cargo, moves: List[Move]) -> None:
        self.cargo = cargo
        self.moves = moves

    def __repr__(self) -> str:
        return f'Cargo: {self.cargo} \n Moves: {self.moves}'

    def process_moves(self, stacked=False):
        for move in self.moves:
            self.cargo.process_move(move, stacked)


def parse_cargo_line(l: str) -> List[str]:
    return [l[4*i+1] for i in range(9)]


def read_ship(filename: str) -> Ship:
    cargo = []
    moves = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            if not l.strip():
                continue
            if '[' in l: 
                cargo.append(parse_cargo_line(l))
            if l.startswith('move'):
                moves.append(Move(l.strip()))
    return Ship(Cargo(cargo), moves)


# Part 1

FILE = 'day5.txt'
ship = read_ship(FILE)
ship.process_moves()
final_result = ship.cargo.get_final_state()
final_result_str = ''.join(final_result)
print(final_result_str)


# Part 2

ship = read_ship(FILE)
ship.process_moves(stacked=True)
final_result = ship.cargo.get_final_state()
final_result_str = ''.join(final_result)
print(final_result_str)
