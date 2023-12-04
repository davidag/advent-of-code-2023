import common as c

numbers_str = {}


def part_one(data: str) -> int:
    numbers = {str(i): i for i in range(1, 10)}
    return sum(extract(line, numbers) for line in c.strings(data))


def part_two(data: str) -> int:
    numbers = {str(i): i for i in range(1, 10)}

    numbers_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers.update({number_str: i for i, number_str in enumerate(numbers_str, 1)})

    return sum(extract(line, numbers) for line in c.strings(data))


def extract(line: str, number_map: dict[str, int]) -> int:
    first_idx = len(line) + 1
    first_num = 0
    for n_str in number_map:
        if (idx := line.find(n_str)) >= 0:
            if idx < first_idx:
                first_idx = idx
                first_num = number_map[n_str]

    last_idx = -1
    last_num = 0
    for n_str in number_map:
        if (idx := line.rfind(n_str)) >= 0:
            if idx > last_idx:
                last_idx = idx
                last_num = number_map[n_str]

    return first_num * 10 + last_num


print(part_one(c.day(1)))
print(part_two(c.day(1)))
