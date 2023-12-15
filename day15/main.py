from functools import reduce


def read_file(filename):
    with open(filename, "r") as f:
        return f.read()[:-1]


def main(filename="./day15/test"):
    input = read_file(filename)
    steps = input.split(",")

    def hash(step):
        def mash(acc, curr):
            acc += ord(curr)
            acc *= 17
            acc %= 256
            return acc

        return reduce(mash, step, 0)

    hashes = list(map(hash, steps))

    summation = reduce(lambda a, b: a + b, hashes)

    print(summation)


main()
main("./day15/input")
