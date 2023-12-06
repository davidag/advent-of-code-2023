import common as c


def part_one(data):
    times, distances = parse_input_one(data)
    total = 1
    for i in range(len(times)):
        total *= calculate_ways(times[i], distances[i]) 
    return total


def part_two(data):
    time, distance = parse_input_two(data)
    return calculate_ways(time, distance) 


def calculate_ways(time, distance) -> int:
    ways = 0
    for t in range(time):
        if (time - t) * t > distance:
            ways += 1
    return ways


def parse_input_one(data):
    lines = c.strings(data)
    return c.ints(lines[0]), c.ints(lines[1])


def parse_input_two(data):
    lines = c.strings(data)
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))
    return time, distance


print(part_one(c.day(6)))
print(part_two(c.day(6)))
