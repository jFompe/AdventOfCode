from math import lcm
from re import findall
from typing import Dict, Tuple


def read_input(filename: str):
    network = {}
    with open(filename, 'r') as f:
        instructions = f.readline().strip()
        f.readline()
        for l in f.readlines():
            a,b,c = findall(r'(\w{3})', l)
            network[a] = (b,c)
        return instructions, network


def follow_network(instructions: str, network: Dict[str, Tuple[str]]) -> int:
    instruction_idx = lambda i : 0 if i == 'L' else 1
    curr = 'AAA'
    steps = 0
    while curr != 'ZZZ':
        curr_instruction = instructions[steps % len(instructions)]
        curr = network[curr][instruction_idx(curr_instruction)]
        steps += 1
    return steps


# Part 1

FILE = 'day8.txt'
instructions, network = read_input(FILE)
print(follow_network(instructions, network))


# Part 2

def follow_network_simultaneous(instructions: str, network: Dict[str, Tuple[str]]) -> int:
    instruction_idx = lambda i : 0 if i == 'L' else 1
    curr = [node for node in network if node[-1] == 'A']
    all_steps = []

    for n in curr:
        steps = 0
        while n[-1] != 'Z':
            curr_instruction = instructions[steps % len(instructions)]
            n = network[n][instruction_idx(curr_instruction)]
            steps += 1
        all_steps.append(steps)
    return lcm(*all_steps)

print(follow_network_simultaneous(instructions, network))
