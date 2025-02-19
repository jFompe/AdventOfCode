from functools import cache


with open('day19.txt', 'r') as f:
    designs = set(f.readline().strip().split(', '))
    f.readline()
    models = [l.strip() for l in f.readlines()]

def is_possible(model) -> bool:
    if model in designs:
        return True
    prefixes = [des for des in designs if model.startswith(des)]
    return any((is_possible(model[len(pref):]) for pref in prefixes))

print(sum(is_possible(model) for model in models))


# Part 2

@cache
def possible_combinations(model) -> int:
    a = 0
    if not model:
        return 0
    if model in designs:
        if len(model) == 1:
            return 1
        else:
            a = 1
    prefixes = [des for des in designs if model.startswith(des)]
    return a + sum(possible_combinations(model[len(pref):]) for pref in prefixes)

print(sum(possible_combinations(model) for model in models))
