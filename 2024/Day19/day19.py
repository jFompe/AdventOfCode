

with open('day19.txt', 'r') as f:
    designs = f.readline().strip().split(', ')
    f.readline()
    models = [l.strip() for l in f.readlines()]

def is_possible(model):
    if any((des == model for des in designs)):
        return True
    prefixes = [des for des in designs if model.startswith(des)]
    return any((is_possible(model[len(pref):]) for pref in prefixes))

print(sum(is_possible(model) for model in models))