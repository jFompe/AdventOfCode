from re import search


def read_input(filename: str):
    with open(filename, 'r') as f:
        return f.readline().strip().split(',')

def apply_hash(seq: str) -> int:
    current_value = 0
    for c in seq:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


# Part 1

FILE = 'day15.txt'
steps = read_input(FILE)
hash_values = map(apply_hash, steps)
print(sum(hash_values))


# Part 2

NUM_BOXES = 256
boxes = [[] for _ in range(NUM_BOXES)]

for step in steps:
    label, operation, focal_length = search(r'([a-z]+)([-=])(\d+)?', step).groups()
    label_value = apply_hash(label)

    index_of_label = next((i for i in range(len(boxes[label_value])) if boxes[label_value][i][0] == label), -1)
    if operation == '-' and index_of_label != -1:
        boxes[label_value].pop(index_of_label)
    if operation == '=':
        if index_of_label == -1:
            boxes[label_value].append((label, int(focal_length)))
        else:
            boxes[label_value][index_of_label] = (label, int(focal_length))

focusing_power = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        focusing_power += (i+1) * (j+1) * lens[1]
print(focusing_power)
