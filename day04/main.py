import re


def read_file(filename):
    with open(filename, 'r') as f:
        return list(filter(lambda l: len(l) > 0, f.read().split("\n")))


def is_empty(line):
    return len(line) > 0


def remove_break(line):
    return line.replace("\n", "")


def parse_input(line):
    m = re.search(r"(?:Card \s*(\d+)): ((?:\s*\d+)+) \| ((?:\s*\d+)+)", line)
    card_num = m.groups()[0]
    all_winning = m.groups()[1]
    winning = list(map(int, re.findall(r"\s*(\d+)\s*", all_winning)))
    all_numbers = m.groups()[2]
    numbers= list(map(int, re.findall(r"\s*(\d+)\s*", all_numbers)))
    return [card_num, winning, numbers]


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
            print(f"card {card} winning number {number}")
            score = (score * 2 if score != 0 else 1)

    return score


def parse_all_input(lines):
    input = []
    for line in lines:
        input.append(parse_input(line))
    return input


def main(filename="./day04/test"):
    lines = read_file(filename)
    input = parse_all_input(lines)

    print(input)
    print(calculate_total_score(input))


main()
main("./day04/input")
