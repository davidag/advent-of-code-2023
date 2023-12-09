import common as c


def part_one(data) -> int:
    histories = parse_input(data)
    return sum(predict(h)[1] for h in histories)


def part_two(data) -> int:
    histories = parse_input(data)
    return sum(predict(h)[0] for h in histories)


def predict(history) -> tuple[int, int]:
    first_values = [history[0]]
    next_value = history[-1]

    diff = list(history)
    while any(value for value in diff):
        for i in reversed(range(1, len(diff))):
            diff[i] = diff[i] - diff[i - 1]
        diff.pop(0)
        first_values.append(diff[0])
        next_value += diff[-1]

    prev_value = 0
    for value in reversed(first_values[:-1]):
        prev_value = value - prev_value

    return prev_value, next_value


def parse_input(data):
    return [c.ints(line) for line in c.strings(data)]


assert part_one(c.day(9)) == 2008960228
assert part_two(c.day(9)) == 1097
