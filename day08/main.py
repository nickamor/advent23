import re


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


def path_length(start, finish, input):
    steps = 0
    current = start
    [directions, paths] = input
    path = []
    while current != finish:
        direction = directions[steps % len(directions)]
        next = paths[current][direction]
        path.append(f"{current} {direction} {next}")
        current = next
        steps += 1
    return steps


def main(filename="./day08/test"):
    lines = read_file(filename)
    start = "AAA"
    end = "ZZZ"
    input = parse_lines(lines)
    print(path_length(start, end, input))


main()
main("./day08/input")
