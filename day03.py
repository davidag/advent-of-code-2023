from collections import defaultdict
from functools import reduce
from operator import mul
import re
import common as c


def part_one(data):
    numbers = parse_input(data)
    return sum(int(n[0]) for n, symbols in numbers.items() if len(symbols) > 0)


def part_two(data):
    numbers = parse_input(data)

    symbols = defaultdict(set)
    for number, adjacent_symbols in numbers.items():
        for symbol in adjacent_symbols:
            symbols[symbol].add(number)

    return sum(
        reduce(mul, [n[0] for n in numbers], 1)
        for s, numbers in symbols.items()
        if s[0] == "*" and len(numbers) == 2
    )


def parse_input(data) -> dict[str, list[str]]:
    lines = c.strings(data)
    numbers = {}
    for number, start, end in find_numbers(lines):
        numbers[(number, *start)] = find_symbols(lines, start, end)
    return numbers


def find_numbers(lines: list[str]):
    p = re.compile(r"\d+")
    for i, line in enumerate(lines):
        for match in re.finditer(p, line):
            yield int(match.group()), (i, match.start()), (i, match.end())


def find_symbols(lines: list[str], start, end) -> list[tuple]:
    result = []
    for i in range(start[0] - 1, start[0] + 2):
        for j in range(start[1] - 1, end[1] + 1):
            if i > 0 and i < len(lines) and j > 0 and j < len(lines[i]):
                char = lines[i][j]
                if char != "." and not char.isdigit():
                    result.append((char, i, j))
    return result


print(part_one(c.day(3)))
print(part_two(c.day(3)))
