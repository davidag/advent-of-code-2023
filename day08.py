from itertools import cycle
import re
import math
import common as c


def part_one(data):
    instructions, network = parse_input(data)
    curr = "AAA"
    for count, ins in enumerate(cycle(instructions), 1):
        dir = 0 if ins == "L" else 1
        curr = network[curr][dir]
        if curr == "ZZZ":
            return count


def part_two(data):
    instructions, network = parse_input(data)
    curr = [src for src in network if src[-1] == "A"]
    for count, ins in enumerate(cycle(instructions), 1):
        dir = 0 if ins == "L" else 1
        for i in range(len(curr)):
            if isinstance(curr[i], str):
                curr[i] = network[curr[i]][dir]
                if curr[i][-1] == "Z":
                    curr[i] = count
        if all(isinstance(c, int) for c in curr):
            break
    return math.lcm(*curr)


def parse_input(data):
    lines = c.strings(data)
    network = {}
    for line in lines[2:]:
        src, left, right = re.findall(r"\w{3}", line)
        network[src] = (left, right)
    return lines[0], network


print(part_one(c.day(8)))
print(part_two(c.day(8)))
