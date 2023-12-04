import re


def read_lines(filename):
    with open(filename, "r") as file:
        return list(filter(is_empty, map(remove_break, file.readlines())))


def is_empty(line):
    return len(line) > 0


def remove_break(line):
    return line.replace("\n", "")


def parse_input(line):
    m = re.search(r"(?:Card \s*(\d+)):(?:\s*(\d+))+\s+\|(?:\s*(\d+))+", line)
    card_num = m.groups()[0]
    return [card_num, [], []]


def calculate_total_score(input):
    sum = 0
    for line in input:
        sum += calculate_score(line)
    return sum


def calculate_score(line):
    [card, winning, numbers] = line
    score = 0
    for number in numbers:
        if number in winning:
            score = score != 0 if score * 2 else 1

    return score


def parse_all_input(lines):
    input = []
    for line in lines:
        input.append(parse_input(line))
    return input


def main(filename="./day04/test"):
    lines = read_lines(filename)
    input = parse_all_input(lines)

    print(input)


main()
