

with open('day5.txt', 'r') as f:
    ranges = []
    while rang := f.readline().strip():
        start, end = map(int, rang.split('-'))
        ranges.append(range(start, end+1))
    ids = [int(ingredient_id) for ingredient_id in f.readlines()]

print(sum(any(ing in rang for rang in ranges) for ing in ids))


# Part 2

class RangeList:

    def __init__(self):
        self.list = []

    def add(self, rang):
        intersections = self._intersections(rang)
        if not intersections:
            self.list.append(rang)
        else:
            self._merge(rang, intersections)

    def compact(self):
        # Not very elegant but easier than improving _merge
        for _ in self.list:
            elem = self.list.pop(0)
            self.add(elem)

    def _merge(self, rang, intersections):
        while intersections:
            inters = intersections.pop(0)
            self.list.remove(inters)
            new_range = range(min(rang.start, inters.start), max(rang.stop, inters.stop))
            self.list.append(new_range)

    def _intersections(self, rang):
        return [r for r in self.list if self._is_intersection(rang, r)]

    def _is_intersection(self, one_rang: range, other_rang: range):
        return one_rang.start <= other_rang.stop and one_rang.stop >= other_rang.start

    def __len__(self):
        return sum(len(r) for r in self.list)


fresh_ids = RangeList()

for rang in ranges:
    fresh_ids.add(rang)
fresh_ids.compact()
fresh_ids.compact()
print(len(fresh_ids))
