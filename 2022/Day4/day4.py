from typing import List, Set


class AssignmentsPair:
    def __init__(self, assignment1: str, assignment2: str) -> None:
        self.assignment1 = self._generate_assignments(assignment1)
        self.assignment2 = self._generate_assignments(assignment2)

    def _generate_assignments(self, assignment) -> Set[int]:
        a1, a2 = assignment.split('-')
        return set(range(int(a1), int(a2)+1))
    
    def __repr__(self) -> str:
        return f'{self.assignment1} {self.assignment2}'

    def is_one_fully_contained(self):
        union = self.assignment1.union(self.assignment2)
        return len(union) == max([len(self.assignment1), len(self.assignment2)])
    
    def are_somewhat_contained(self):
        return len(self.assignment1.intersection(self.assignment2)) != 0

def read_assignments(filename: str) -> List[AssignmentsPair]:
    with open(filename, 'r') as f:
        return [AssignmentsPair(*l.strip().split(',')) for l in f.readlines()]


# Part 1

FILE = 'day4.txt'
assignments = read_assignments(FILE)
are_fully_contained = [ap.is_one_fully_contained() for ap in assignments]
num_fully_contained = sum(are_fully_contained)
print(num_fully_contained)


# Part 2
are_somewhat_contained = [ap.are_somewhat_contained() for ap in assignments]
num_somewhat_contained = sum(are_somewhat_contained)
print(num_somewhat_contained)
