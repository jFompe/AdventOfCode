from re import match
from typing import List, Tuple
from functools import reduce


def read_input(filename: str) -> Tuple[List[int], List[Tuple[int, range]]]:
    mappings = []
    mapping_group = None
    with open(filename, 'r') as f:
        seeds = list(map(int, f.readline().strip().removeprefix('seeds: ').split(' ')))
        for l in f.readlines():
            if not l.strip() or match(r'[a-z].+', l):
                if mapping_group:
                    mappings.append(mapping_group)
                mapping_group = []
            else:
                # Destination Range Start, Source Range Start, Range Length
                drs, srs, rl = map(int, l.strip().split(' '))
                mapping_group.append((drs, range(srs, srs+rl)))
    mappings.append(mapping_group)
    return seeds, mappings

def map_seed_into_range(seed: int, drs: int, source_range: range) -> int:
    return drs + seed - source_range.start

def map_seeds(seeds: List[int], mappings_group: Tuple[int, range]):
    def map_seed(seed: int, mappings_group: Tuple[int, range]) -> int:
        return next((map_seed_into_range(seed, drs, map_range) for drs, map_range in mappings_group if seed in map_range), seed)

    return [map_seed(s, mappings_group) for s in seeds]


# Part 1

FILE = 'day5.txt'
seeds, mappings = read_input(FILE)
mapped_seeds = reduce(lambda s,m : map_seeds(s, m), mappings, seeds)
print(min(mapped_seeds))


# Part 2

def seeds_by_ranges(seeds_list: List[int]):
    return [range(seeds_list[i], seeds_list[i]+seeds_list[i+1]) for i in range(0, len(seeds_list), 2)]

def map_seeds_ranges(seeds_ranges, mappings):
    def map_seeds_range(seeds_range):
        if seeds_range.start == seeds_range.stop:
            return []
        for drs, map_range in mappings:
            if seeds_range.start in map_range and seeds_range.stop-1 in map_range:
                # Case seed_range fully contained in map_range
                return [range(drs + seeds_range.start - map_range.start, drs + seeds_range.stop - map_range.start)]
            if map_range.start in seeds_range and map_range.stop-1 in seeds_range:
                # Case map_range contained in seed_range
                return map_seeds_range(range(seeds_range.start, map_range.start)) + [range(drs + map_range.start - map_range.start, drs + map_range.stop - map_range.start)] + map_seeds_range(range(map_range.stop, seeds_range.stop))
            if seeds_range.start in map_range: # and seeds_range.stop-1 not in map_range
                # Case seeds_range.start in map_range but seeds_range.stop-1 is not
                return [range(drs + seeds_range.start - map_range.start, drs + map_range.stop - map_range.start)] + map_seeds_range(range(map_range.stop, seeds_range.stop))
            if seeds_range.stop-1 in map_range: # and seeds_range.start not in map_range
                # Case seeds_range.stop-1 in map_range but seeds_range.start is not
                return map_seeds_range(range(seeds_range.start, map_range.start)) + [range(drs + map_range.start - map_range.start, drs + seeds_range.stop - map_range.start)]
        return [seeds_range]
    
    return [sr for seeds_range in seeds_ranges for sr in map_seeds_range(seeds_range)]

mapped_seeds = reduce(lambda s,m : map_seeds_ranges(s, m), mappings, seeds_by_ranges(seeds))
print(min([sr.start for sr in mapped_seeds]))
