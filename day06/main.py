import re
from turtle import distance

def read_file(filename):
    with open(filename, 'r') as f:
        return list(filter(lambda l: len(l) > 0, f.read().split("\n")))


def parse_input(lines):
    times = re.findall(r"\d+", lines[0])
    distances = re.findall(r"\d+", lines[1])
    input = []
    for i in range(len(times)):
        input.append([int(times[i]), int(distances[i])])
    return input


def find_all_strategies(input):
    strats = []
    for race in input:
        [time, distance] = race
        race_strats = []
        for i in range(1, time):
            if i * (time - i) > distance:
                race_strats.append(i)
        strats.append(race_strats)
    return strats


def find_strategy_count(input):
    strats = []
    for race in input:
        [time, distance] = race
        race_strats = 0
        for i in range(1, time):
            if i * (time - i) > distance:
                race_strats += 1
        strats.append(race_strats)
    return strats


def map_to_size(strats):
    sizes = []
    for s in strats:
        sizes.append(len(s))
    return sizes


def reduce_multiply(numbers):
    retvar = 1
    for n in numbers:
        retvar *= n
    return retvar


def fixed_parse_input(lines):
    times = ''
    for r in re.findall(r"\d+", lines[0]):
        times += r
    distances = ''
    for r in re.findall(r"\d+", lines[1]):
        distances += r
    return [[int(times), int(distances)]]


def main(filename="./day06/test"):
    lines = read_file(filename)
    input = parse_input(lines)
    part1 = reduce_multiply(find_strategy_count(input))
    part2 = find_strategy_count(fixed_parse_input(lines))[0]
    print(f"{part1}, {part2}")


main()
main("./day06/input")
