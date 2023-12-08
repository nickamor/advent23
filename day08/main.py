import re
import functools


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")[:-1]


def parse_lines(lines):
    directions = lines[0]
    paths = {}
    for line in lines[2:]:
        a = re.search(r"(...) = \((...), (...)\)", line)
        paths[a[1]] = {"L": a[2], "R": a[3]}
    return (directions, paths)


def find_next_step(current, steps, input):
    [directions, paths] = input
    direction = directions[steps % len(directions)]
    return paths[current][direction]


def traverse_path(start, finish, input):
    current = start
    path = []
    while re.search(finish, current) == None:
        next = find_next_step(current, len(path), input)
        path.append(f"{current} -> {next}")
        current = next
    return path


def ghost_done(finish, currents):
    for key, value in currents.items():
        if re.search(finish, value) == None:
            return False
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def lcmm(args):
    return functools.reduce(lcm, args)


def ghost_traverse(start, finish, input):
    [directions, paths] = input
    currents = {}
    steps = 0
    for key in paths.keys():
        if re.search(start, key) != None:
            currents[key] = key
    # while not ghost_done(finish, currents):
    #     for k, v in currents.items():
    #         currents[k] = find_next_step(v, steps, input)
    #     steps += 1

    path_lengths = {}
    for key in currents.keys():
        path_lengths[key] = len(traverse_path(key, finish, input))

    return lcmm(path_lengths.values())


def main(filename="./day08/test2"):
    lines = read_file(filename)
    input = parse_lines(lines)
    # path = traverse_path("AAA", "ZZZ", input)
    paths = ghost_traverse("..A", "..Z", input)
    # print(len(path))
    print(paths)


main()
main("./day08/input")
