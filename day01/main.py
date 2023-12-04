
def read_file(filename):
    with open(filename, 'r') as f:
        return list(filter(lambda l: len(l) > 0, f.read().split("\n")))


def extract_values(line):
    return list(filter(str.isdigit, line))


def get_word_value(str):
    words = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }.items()
    for key, value in words:
        if str.startswith(key):
            return value


def extract_values_map(line):
    values = []
    for pos, char in enumerate(line):
        if char.isdigit():
            values.append(char)
            continue
        value = get_word_value(line[pos:])
        if value != None:
            values.append(value)
            continue
    return values


def sum(numbers):
    s = 0
    for n in numbers:
        s += n
    return s


def main(filename="./day01/test1"):
    lines = read_file(filename)

    easy_values = []
    for line in lines:
        values = extract_values(line)
        if (len(values) > 0): # the simple approach fails on test2
            easy_values.append(int(values[0] + values[-1]))

    hard_values = []
    for line in lines:
        values = extract_values_map(line)
        hard_values.append(int(values[0] + values[-1]))

    print(f"{sum(easy_values)}, {sum(hard_values)}")

main()
main("./day01/test2")
main("./day01/input")
