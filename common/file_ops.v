module common

import os

pub fn read_example(n int, letter string) !string {
    filename := './inputs/example${n:02}${letter}'
    return os.read_file(filename)
}

pub fn read_input(n int) !string {
    filename := './inputs/input${n:02}'
    return os.read_file(filename)
}
