import re
import functools


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")[:-1]


def line_read(line):
    return list(map(int, re.findall(r"\d+", line)))


def grade(numbers):
    return max(*numbers) - min(*numbers)


def variation(numbers):
    v = []
    for i in range(len(numbers) - 1):
        v.append(numbers[i + 1] - numbers[i])
    return v


def predict_weather(numbers):
    if grade(numbers) == 0:
        return numbers[-1]

    var = variation(numbers)

    return numbers[-1] + predict_weather(var)


def sum(numbers):
    return functools.reduce(lambda x, y: x + y, numbers)


def main(filename="./day09/test"):
    lines = read_file(filename)
    numbers = list(map(line_read, lines))
    for l in numbers:
        v = l
        while any(map(lambda n: n != 0, v)):
            print(f"  {v}  {predict_weather(v)}")
            v = variation(v)
        print(" ")
    calc = list(map(predict_weather, numbers))
    print(calc)
    print(sum(calc))


main()
# main("./day09/input")
