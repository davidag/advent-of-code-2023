import arrays

fn part_one(data string) !int {
        number_map := {
                '1': 1
                '2': 2
                '3': 3
                '4': 4
                '5': 5
                '6': 6
                '7': 7
                '8': 8
                '9': 9
        }
        nums := parse_input(data, number_map)
        return arrays.sum[int](nums)!
}

fn part_two(data string) !int {
        number_map := {
                '1':     1
                '2':     2
                '3':     3
                '4':     4
                '5':     5
                '6':     6
                '7':     7
                '8':     8
                '9':     9
                'one':   1
                'two':   2
                'three': 3
                'four':  4
                'five':  5
                'six':   6
                'seven': 7
                'eight': 8
                'nine':  9
        }
        nums := parse_input(data, number_map)
        return arrays.sum[int](nums)!
}

fn extract(line string, number_map map[string]int) int {
        mut first_idx := line.len + 1
        mut first_num := 0
        for n_str, _ in number_map {
                if idx := line.index(n_str) {
                        if idx < first_idx {
                                first_idx = idx
                                first_num = number_map[n_str]
                        }
                }
        }

        mut last_idx := -1
        mut last_num := 0
        for n_str, _ in number_map {
                if idx := line.last_index(n_str) {
                        if idx > last_idx {
                                last_idx = idx
                                last_num = number_map[n_str]
                        }
                }
        }

        return first_num * 10 + last_num
}

fn parse_input(data string, number_map map[string]int) []int {
        mut nums := []int{}
        for line in data.split_into_lines() {
                nums << extract(line, number_map)
        }
        return nums
}

fn read_example(n int, letter string) !string {
    filename := './inputs/example${n:02}${letter}'
    return os.read_file(filename)
}

fn read_input(n int) !string {
    filename := './inputs/input${n:02}'
    return os.read_file(filename)
}

fn main() {
        println(part_one(read_input(1)!)!)
        println(part_two(read_input(1)!)!)
}
