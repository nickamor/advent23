import re


def read_file(filename):
    with open(filename, 'r') as f:
        return list(filter(lambda l: len(l) > 0, f.read().split("\n")))


def parse_input(lines):
    symbols=[]
    numbers=[]
    for row, line in enumerate(lines):
        for match in re.finditer(r"[^\.\d\s]", line):
            symbols.append([row, match.span()[0], match.group()])
        for match in re.finditer(r"\d+", line):
            numbers.append([row, match.span(), int(match.group())])
    return [symbols, numbers]


def get_adjacencies(row, columns):
    a=[[row, columns[0] - 1], [row, columns[1]]]
    for i in range(columns[0] - 1, columns[1] + 1):
        a.append([row - 1, i])
        a.append([row + 1, i])
    return a


def sum(numbers):
    s = 0
    for n in numbers:
        s += n
    return s


def main(filename="./day03/test"):
    lines = read_file(filename)

    [all_symbols, all_numbers] = parse_input(lines)

    part_ids=[]
    gear_ratios=[]
    for symbol in all_symbols:
        [s_row, s_col, s]=symbol

        gear_ids=[]
        for number in all_numbers:
            [n_row, n_columns, n] = number

            if [s_row, s_col] in get_adjacencies(n_row, n_columns):
                part_ids.append(n)
                if s=="*":
                    gear_ids.append(n)

        if len(gear_ids) == 2:
            gear_ratios.append(gear_ids[0] * gear_ids[1])

    print(f"{sum(part_ids)}, {sum(gear_ratios)}")


main()
main("./day03/input")
