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
    card_num = int(m.groups()[0])
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


def winning_numbers(line):
    [card, winning, numbers] = line
    win=[]
    for number in numbers:
        if number in winning:
            win.append(number)
    return win


def calculate_score(line):
    score = 0
    for number in winning_numbers(line):
        score = (score * 2 if score != 0 else 1)

    return score


def parse_all_input(lines):
    input = []
    for line in lines:
        input.append(parse_input(line))
    return input


def count_cards(input):
    cards={}
    for line in input:
        [card, winning, numbers] = line
        cards[card] = 1
    
    for line in input:
        [card, winning, numbers] = line
        c = cards[card]
        wins = len(winning_numbers(line))
        for i in range(card + 1, card + 1 + wins):
            cards[i] += c

    total_cards=0
    for key, value in cards.items():
        total_cards += value

    return total_cards


def main(filename="./day04/test"):
    lines = read_file(filename)
    input = parse_all_input(lines)

    print(f"{calculate_total_score(input)}, {count_cards(input)}")


main()
main("./day04/input")
