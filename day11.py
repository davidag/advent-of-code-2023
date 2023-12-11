from itertools import combinations
import common as c


def solution(data, expansion):
    map = parse_input(data)
    galaxies = find_galaxies(map)
    galaxies = expand_galaxies(map, galaxies, expansion)
    total = 0
    for g1, g2 in combinations(galaxies, 2):
        total += c.manhattan(g1, g2)
    return total


def find_galaxies(map):
    return [
        (i, j)
        for i, row in enumerate(map)
        for j, value in enumerate(row)
        if value == "#"
    ]


def expand_galaxies(map, galaxies, expansion):
    old_galaxies = dict(enumerate(galaxies))
    new_galaxies = old_galaxies.copy()
    empty_rows = [i for i in range(len(map)) if all(i != r for r, _ in galaxies)]
    empty_cols = [j for j in range(len(map)) if all(j != c for _, c in galaxies)]

    # Expand galaxy rows
    for i in range(len(map)):
        if i in empty_rows:
            num_empty_rows = empty_rows.index(i) + 1
            for g_id, (r, _) in old_galaxies.items():
                if r > i:
                    new_galaxies[g_id] = (
                        old_galaxies[g_id][0] + (num_empty_rows * expansion),
                        old_galaxies[g_id][1],
                    )

    # Expand galaxy cols
    for j in range(len(map[0])):
        if j in empty_cols:
            num_empty_cols = empty_cols.index(j) + 1
            for g_id, (_, c) in old_galaxies.items():
                if c > j:
                    new_galaxies[g_id] = (
                        new_galaxies[g_id][0],
                        old_galaxies[g_id][1] + (num_empty_cols * expansion),
                    )

    return new_galaxies.values()


def parse_input(data):
    return [[v for v in line] for line in c.strings(data)]


print(solution(c.day(11), 2 - 1))
print(solution(c.day(11), 1000000 - 1))
