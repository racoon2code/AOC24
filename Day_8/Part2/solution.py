import itertools
from collections import defaultdict
from time import time


def measure_runtime(fn):
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()        
        return result
    return wrapper


def get_input(filename: str):
    with open(filename) as file:
        return [line.rstrip() for line in file]


def create_antenna_map(lines: list):
    antenna_map = defaultdict(list)
    for r, l in enumerate(lines):
        for c, el in enumerate(l):
            if el != '.':
                antenna_map[el].append((r, c))
    return antenna_map


def check_validity_of_candidate(candidate: tuple, max_rows: int, max_cols: int):
    return 0 <= candidate[0] < max_rows and 0 <= candidate[1] < max_cols


def get_candidate_antinodes_part_1(pair: list):
    vec = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
    a = (pair[1][0] + vec[0], pair[1][1] + vec[1])
    b = (pair[0][0] - vec[0], pair[0][1] - vec[1])
    return [a, b]


def get_candidate_antinodes_part_2(pair: list, max_rows: int, max_cols: int):
    candidates = []
    vec = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
    b, a = pair
    candidates.extend(pair)
    search_a, search_b = True, True
    while search_a or search_b:
        if search_a:
            a = (a[0] + vec[0], a[1] + vec[1])
        if search_b:
            b = (b[0] - vec[0], b[1] - vec[1])
        if check_validity_of_candidate(a, max_rows, max_cols):
            candidates.append(a)
        else:
            search_a = False
        if check_validity_of_candidate(b, max_rows, max_cols):
            candidates.append(b)
        else:
            search_b = False
    return candidates


# Part 2 solution
@measure_runtime
def part2(antenna_map: dict, max_rows: int, max_cols: int):
    antinodes = set()
    for locations in antenna_map.values():
        candidates = list(itertools.chain.from_iterable(
            [get_candidate_antinodes_part_2(p, max_rows, max_cols) for p in itertools.combinations(locations, 2)]
        ))
        antinodes.update(candidates)
    print(f"Total number of antinodes: {len(antinodes)}")


lines = get_input("input.txt")  # Change to your input file
max_rows, max_cols = len(lines), len(lines[0])
antenna_map = create_antenna_map(lines)


part2(antenna_map, max_rows, max_cols)
