import common as c


def part_one(data):
    grid, start, _, _ = parse_input(data)
    graph = create_graph(grid)
    path = follow_loop(graph, start, start)
    return len(path) // 2


def create_graph(grid):
    return {pos: connected_positions(grid, pos) for pos in grid}


def follow_loop(graph, start, end) -> list[tuple]:
    stack = [(start, [start])]
    seen = set()
    while len(stack) > 0:
        curr, path = stack.pop()
        seen.add(curr)
        for pos in graph[curr]:
            if pos == end and len(path) > 2:
                return path + [pos]
            if pos not in seen:
                stack.append((pos, path + [pos]))
    return []


def connected_positions(grid, curr) -> list[tuple[int]]:
    dirs = {
        "R": (curr[0], curr[1] + 1),
        "B": (curr[0] + 1, curr[1]),
        "L": (curr[0], curr[1] - 1),
        "T": (curr[0] - 1, curr[1]),
    }
    value = grid[curr]
    result = []
    if value in "-FL" and grid.get(dirs["R"], "X") in "J-7":
        result.append(dirs["R"])
    if value in "|F7" and grid.get(dirs["B"], "X") in "J|L":
        result.append(dirs["B"])
    if value in "-J7" and grid.get(dirs["L"], "X") in "F-L":
        result.append(dirs["L"])
    if value in "|JL" and grid.get(dirs["T"], "X") in "F|7":
        result.append(dirs["T"])
    return result


def part_two(data):
    grid, start, rows, cols = parse_input(data)
    graph = create_graph(grid)
    path = follow_loop(graph, start, start)
    return len(find_enclosed(grid, rows, cols, path))


def find_enclosed(grid, rows, cols, path) -> set[tuple]:
    down = {"|", "7", "F"}
    found = set()
    for i in range(rows):
        up = False
        for j in range(cols):
            if grid.get((i, j), "X") in down and (i, j) in path:
                up = not up
            if up and (i, j) not in path:
                found.add((i, j))
    return found


def parse_input(data):
    grid = {}
    start = (-1, -1)
    lines = c.strings(data)
    for i, line in enumerate(lines):
        for j, value in enumerate(line):
            grid[(i, j)] = value
            if value == "S":
                start = (i, j)
    fill_start_position(grid, start)
    return grid, start, len(lines), len(lines[0])


def fill_start_position(grid, start):
    dirs = {
        "R": (start[0], start[1] + 1),
        "B": (start[0] + 1, start[1]),
        "L": (start[0], start[1] - 1),
        "T": (start[0] - 1, start[1]),
    }
    if grid.get(dirs["R"], "X") in "-J7":
        if grid.get(dirs["B"], "X") in "|JL":
            grid[start] = "F"
        elif grid.get(dirs["T"], "X") in "|F7":
            grid[start] = "L"
        else:
            grid[start] = "-"
    elif grid.get(dirs["B"], "X") in "|LJ":
        if grid.get(dirs["T"], "X") in "|7F":
            grid[start] = "|"
        else:
            grid[start] = "7"
    elif grid.get(dirs["L"], "X") in "-FL":
        grid[start] = "J"


print(part_one(c.day(10)))
print(part_two(c.day(10)))
