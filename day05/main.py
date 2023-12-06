import re

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().split("\n")


def seeds_to_plant(input):
    line = input[0]
    seeds = list(map(int, re.findall(r"\d+", line)))
    return seeds


def parse_seeds(line):
    seeds = list(map(int, re.findall(r"\d+", line)))
    return seeds


def parse_map_line(line):
    ns = list(map(int, re.findall(r"\d+", line)))
    return ns


def parse_map(lines):
    title = re.search(r"(.*) map:", lines[0]).groups()[0]
    points = list(map(parse_map_line, lines[1:]))
    return [title, points]


def parse_input(lines):
    seeds=[]
    maps=[]
    current_map=[]
    for idx, line in enumerate(lines):
        if idx == 0:
            seeds = parse_seeds(line)
        elif idx == 1:
            continue
        elif len(line) == 0:
            maps.append(parse_map(current_map))
            current_map = []
        else:
            current_map.append(line)
    return [seeds, maps]


def get_destination(source, map):
    [title, points] = map
    for pointy in points:
        [p_dest, p_source, p_len] = pointy
        if source >= p_source and source < p_source + p_len:
            return p_dest + (source - p_source)
    return source


def find_seed_locations(input):
    [seeds, maps] = input
    locations = []
    for seed in seeds:
        current = seed
        for map in maps:
            current = get_destination(current, map)
        locations.append(current)
    return locations


def reduce_min(locations):
    return sorted(locations)[0]


def main(filename="./day05/test"):
    lines = read_file(filename)
    input = parse_input(lines)
    part1 = reduce_min(find_seed_locations(input))
    print(part1)


main()
main("./day05/input")
