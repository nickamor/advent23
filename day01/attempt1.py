debug = False
# debug = True


def read_lines(filename):
    with open(filename, "r") as file:
        return list(filter(is_empty, map(remove_break, file.readlines())))


def is_empty(line):
    return len(line) > 0


def remove_break(line):
    return line.replace("\n", "")


def debug_print(string):
    if debug == True:
        print(string)


def replace_words(line):
    digit_words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }.items()

    for i in range(len(line)):
        substr = line[i:]
        for word, digit in digit_words:
            if substr.find(word) == 0:
                v = ""
                v += line[:i]
                v += substr.replace(word, digit)
                return replace_words(v)

    return line


def get_digits(line):
    return list(filter(str.isdigit, replace_words(line)))


def extract_value(line):
    line = replace_words(line)
    line = get_digits(line)
    return int(line[0] + line[-1])


def main(filename="./day01/input"):
    lines = read_lines(filename)
    sum = 0

    debug_print("line,with_digits,only_digits,value")

    for line in lines:
        with_digits = replace_words(line)
        only_digits = get_digits(with_digits)
        value = extract_value(line)

        debug_print(f"{line},{with_digits},{''.join(only_digits)},{value}")

        sum += value

    debug_print("\n")

    print(sum)


main()
