


with open('day5.txt', 'r') as f:
    orders = set()
    while l := f.readline():
        line = l.strip()
        if not line:
            break
        orders.add(tuple(int(n) for n in line.split('|')))

    updates = []
    for l in f.readlines():
        line = l.strip()
        updates.append(tuple(int(n) for n in line.split(',')))


# PART 1

def is_valid_update(update):
    for i in range(0, len(update) - 1):
        for j in range(i + 1, len(update)):
            if (update[j], update[i]) in orders:
                return False
    return True

total = 0
for update in updates:
    if is_valid_update(update):
        total += update[len(update) // 2]
print(total)


# PART 2

def reorder_update(update):
    relevant_orders = []
    for n in update:
        for order in orders:
            if n in order:
                relevant_orders.append(order)

    reordered = []
    pages = set(update)
    while pages:
        lefts = { n: 0 for n in pages }
        for order in relevant_orders:
            if order[0] in lefts:
                lefts[order[0]] += 1
        left_key = max(lefts, key=lefts.get)
        reordered.append(left_key)
        pages.remove(left_key)
    return reordered

incorrect_updates = [update for update in updates if not is_valid_update(update)]
total = 0
for update in incorrect_updates:
    reordered = reorder_update(update)
    total += reordered[len(reordered) // 2]
print(total)

