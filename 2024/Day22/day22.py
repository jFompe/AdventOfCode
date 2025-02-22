

with open('day22.txt', 'r') as f:
    secret_numbers = [int(l.strip()) for l in f.readlines()]

prune = lambda x: x % 16777216

def evolve_step(number: int) -> int:
    number = prune(number * 64 ^ number)
    number = prune(number // 32 ^ number)
    number = prune(number * 2048 ^ number)
    return number

def evolve(number: int, steps: int) -> int:
    for _ in range(steps):
        number = evolve_step(number)
    return number

total = sum(evolve(n, 2000) for n in secret_numbers)
print(total)


# Part 2

def changes_sequence(number: int, steps: int):
    sequence = []
    for _ in range(steps):
        next_number = evolve_step(number)
        sequence.append((next_number % 10, next_number % 10 - number % 10))
        number = next_number
    return sequence

def group_sequence(sequence):
    groups = {}
    for i in range(len(sequence) - 4):
        seq = tuple(s[1] for s in sequence[i:i+4])
        if seq not in groups:
            groups[seq] = sequence[i+3][0]
    return groups


sequences_per_number = [changes_sequence(n, 2001) for n in secret_numbers] # For some reason I need to use 2001 instead of 2000
grouped_sequences = [group_sequence(sequence) for sequence in sequences_per_number]

all_sequences = set(seq for sequences in grouped_sequences for seq in sequences)

cost_per_sequence = {}
for sequence in all_sequences:
    if sequence not in cost_per_sequence:
        cost_per_sequence[sequence] = 0

    for grouped in grouped_sequences:
        if sequence in grouped:
            cost_per_sequence[sequence] += grouped[sequence]

print(cost_per_sequence[max(cost_per_sequence, key=lambda x: cost_per_sequence[x])])