import common as c
import re


def part_one(data):
    spring_rows = parse_input(data)
    total = 0
    for records, cgroups in spring_rows:
        total += arrangements(records, cgroups)
    return total


def arrangements(records, cgroups) -> int:
    def search_r(idx):
        if idx == len(r):
            return valid("".join(r), cgroups)
        if r[idx] == "?":
            total = 0
            for p in ['.', '#']:
                r[idx] = p
                total += search_r(idx + 1)
            r[idx] = "?"
            return total
        else:
            return search_r(idx + 1)

    r = list(records)
    return search_r(0)


def valid(records, cgroups):
    groups = re.findall(r"#+", records)
    if len(groups) != len(cgroups):
        return 0
    for i, group in enumerate(groups):
        if len(group) != cgroups[i]:
            return 0
    return 1


def parse_input(data):
    rows = []
    for line in c.strings(data):
        record, groups = line.split()
        rows.append((record, [int(g) for g in groups.split(",")]))
    return rows


# print(part_one(c.day(12)))
print(part_two(c.example(12, "a")))
