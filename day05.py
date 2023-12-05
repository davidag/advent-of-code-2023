import bisect
from collections import namedtuple
import common as c


Range = namedtuple("Range", ["start", "end"])


def part_one(data):
    seeds, map_ranges = parse_input(data)
    curr_ranges = sorted([Range(seed, seed) for seed in seeds])
    for m in range(len(map_ranges)):
        curr_ranges = [r for r in get_ranges(curr_ranges, map_ranges[m])]
        curr_ranges = merge_ranges(curr_ranges)
    return curr_ranges[0][0]


def part_two(data):
    seeds, map_ranges = parse_input(data)
    curr_ranges = sorted(
        [Range(start, start + length - 1) for start, length in c.chunked(seeds, 2)]
    )
    for m in range(len(map_ranges)):
        curr_ranges = [r for r in get_ranges(curr_ranges, map_ranges[m])]
        curr_ranges = merge_ranges(curr_ranges)
    return curr_ranges[0][0]


def get_ranges(curr_ranges, map_ranges):
    ci, mi = 0, 0
    while ci < len(curr_ranges) and mi < len(map_ranges):
        curr, (src, dst) = curr_ranges[ci], map_ranges[mi]
        if curr.end < src.start:
            yield curr
            ci += 1
            continue

        if curr.start > src.end:
            mi += 1
            continue

        if curr.start < src.start:
            yield Range(curr.start, src.start - 1)
            if curr.end <= src.end:
                yield Range(dst.start, dst.start + curr.end - src.start)
                ci += 1
            else:
                yield Range(dst.start, dst.end)
                curr_ranges[ci] = Range(src.end, curr.end)
                mi += 1
        else:
            if curr.end <= src.end:
                yield Range(
                    dst.start + curr.start - src.start, dst.start + curr.end - src.start
                )
                ci += 1
            else:
                yield Range(dst.start + curr.start - src.start, dst.end)
                curr_ranges[ci] = Range(src.end, curr.end)
                mi += 1

    if ci < len(curr_ranges):
        for ci in range(ci, len(curr_ranges)):
            yield curr_ranges[ci]


def merge_ranges(ranges: list[tuple]) -> list[tuple]:
    ranges.sort()
    merged_ranges = [ranges[0]]
    for cur_start, cur_end in ranges[1:]:
        last_start, last_end = merged_ranges[-1]
        if cur_start <= last_end + 1:
            merged_ranges[-1] = Range(last_start, max(last_end, cur_end))
        else:
            merged_ranges.append(Range(cur_start, cur_end))
    return merged_ranges


def parse_input(data) -> tuple[tuple[int], list[list]]:
    lines = c.strings(data)
    seeds = c.ints(lines[0])
    map_ranges = []
    i = 1
    while i < len(lines):
        if lines[i].endswith("map:"):
            map_ranges.append([])
        elif len(lines[i]) > 0:
            dst_start, src_start, range_len = c.ints(lines[i])
            bisect.insort(
                map_ranges[-1],
                (
                    Range(src_start, src_start + range_len - 1),
                    Range(dst_start, dst_start + range_len - 1),
                ),
            )
        i += 1

    return seeds, map_ranges


print(part_one(c.day(5)))
print(part_two(c.day(5)))
