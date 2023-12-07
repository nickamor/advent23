import re


def read_file(filename):
    with open(filename, 'r') as f:
        return list(filter(lambda l: len(l) > 0, f.read().split("\n")))


def parse_line(line):
    x = line.split(" ")
    return (x[0], int(x[1]))


def parse_input(lines):
    return list(map(parse_line, lines))

label_strength = {
    'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1
}

def hand_ranking(line):
    [hand, _wager] = line
    counts = {
        'A': 0,
        'K': 0,
        'Q': 0,
        'J': 0,
        'T': 0,
        '9': 0,
        '8': 0,
        '7': 0,
        '6': 0,
        '5': 0,
        '4': 0,
        '3': 0,
        '2': 0
    }
    base_score = 0
    for c in hand:
        counts[c] += 1
        base_score += label_strength[c] << 1
    type_score = 0
    cc = sorted(counts.items(), key=lambda i: -i[1])
    if cc[0][1] == 5:
        # Five of a kind
        type_score = 7
    if cc[0][1] == 4:
        # Four of a kind
        type_score = 6
    if cc[0][1] == 3 and cc[1][1]:
        # Full house
        type_score = 5
    if cc[0][1] == 3:
        # Three of a kind
        type_score = 4
    if cc[0][1] == 2 and cc[1][1] == 2:
        # Two pair
        type_score = 3
    if cc[0][1] == 2:
        # One pair
        type_score = 2
    if cc[0][1] == 1:
        # High card
        type_score = 1

    return base_score << type_score


def score_ranking(input):
    s = sorted(input, key=hand_ranking)
    out = []
    for i, hand in enumerate(s):
        out.append((hand, (i + 1) * hand[1]))
    return out


def reduce_total(input):
    sum = 0
    for i in input:
        sum += i[1]
    return sum


def main(filename="./day07/test"):
    lines = read_file(filename)
    input = parse_input(lines)
    # input = list(map(lambda l: (l, hand_ranking(l), input)))
    print(reduce_total(score_ranking(input)))


main()
# main("./day07/input")
