import re


def read_file(filename):
    with open(filename, "r") as f:
        return list(filter(lambda l: len(l) > 0, f.read().split("\n")))


def parse_line(line):
    x = line.split(" ")
    return (x[0], int(x[1]))


def parse_input(lines):
    return list(map(parse_line, lines))


label_strength = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "J": "D",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M",
}

label_strength_joker = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M",
    "J": "X",
}


def get_hand_type(hand):
    counts = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "J": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
    }
    for card in hand:
        counts[card] += 1

    counted = sorted(counts.items(), key=lambda i: -i[1])
    if counted[0][1] == 5:
        # Five of a kind
        return "A"
    elif counted[0][1] == 4:
        # Four of a kind
        return "B"
    elif counted[0][1] == 3 and counted[1][1] == 2:
        # Full house
        return "C"
    elif counted[0][1] == 3:
        # Three of a kind
        return "D"
    elif counted[0][1] == 2 and counted[1][1] == 2:
        # Two pair
        return "E"
    elif counted[0][1] == 2:
        # One pair
        return "F"
    else:
        # High card
        return "G"


def get_hand_type_jorker(hand):
    counts = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
    }
    counts_j = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
    }
    for card in hand:
        if card == "J":
            for c in counts_j:
                counts_j[c] += 1
        else:
            counts[card] += 1
            counts_j[card] += 1

    counted = sorted(counts.items(), key=lambda i: -i[1])
    counted_j = sorted(counts_j.items(), key=lambda i: -i[1])
    if counted_j[0][1] == 5:
        # Five of a kind
        return "A"
    elif counted_j[0][1] == 4:
        # Four of a kind
        return "B"
    elif counted_j[0][1] == 3 and counted_j[1][1] == 2:
        # Full house
        return "C"
    elif counted_j[0][1] == 3:
        # Three of a kind
        return "D"
    elif counted_j[0][1] == 2 and counted_j[1][1] == 2:
        # Two pair
        return "E"
    elif counted_j[0][1] == 2:
        # One pair
        return "F"
    else:
        # High card
        return "G"


def hand_ranking(line):
    [hand, _wager] = line
    base_score = ""
    for card in hand:
        base_score += label_strength[card]

    return get_hand_type(hand) + base_score


def hand_ranking_jokerfied(line):
    [hand, _wager] = line
    base_score = ""
    for card in hand:
        base_score += label_strength[card]

    return get_hand_type_jorker(hand) + base_score


def score_ranking(input):
    s = sorted(input, key=hand_ranking, reverse=True)
    out = []
    for i, hand in enumerate(s):
        out.append((hand, (i + 1) * hand[1]))
    return out


def score_ranking_jk(input):
    s = sorted(input, key=hand_ranking_jokerfied, reverse=True)
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
    # print(list(map(lambda l: (l, hand_ranking(l)), input)))
    print(reduce_total(score_ranking(input)))
    print(reduce_total(score_ranking_jk(input)))


main()
main("./day07/input")
