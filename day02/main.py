import re


def read_lines(filename):
    with open(filename, "r") as file:
        return list(filter(is_empty, map(remove_break, file.readlines())))


def is_empty(line):
    return len(line) > 0


def remove_break(line):
    return line.replace("\n", "")


def parse_round(round):
    r = 0
    g = 0
    b = 0
    if round.find("red") >= 0:
        r = int(re.search("(\d+) red", round).group(1))
    if round.find("green") >= 0:
        g = int(re.search("(\d+) green", round).group(1))
    if round.find("blue") >= 0:
        b = int(re.search("(\d+) blue", round).group(1))
    return [r, g, b]


def parse_games(lines):
    all = []
    for line in lines:
        [id_string, all_rounds] = line.split(": ")
        rounds_string = all_rounds.split("; ")
        id = int(re.search("Game (\d+)", id_string).group(1))
        rounds = list(map(parse_round, rounds_string))
        all.append([id, rounds])
    return all


def is_possible(r, g, b, game):
    [_id, rounds] = game
    for round in rounds:
        [gr, gg, gb] = round
        if gr > r or gb > b or gg > g:
            return False
    return True


def game_solve(game):
    r = 0
    g = 0
    b = 0
    [_id, rounds] = game
    for round in rounds:
        [rr, rg, rb] = round
        r = max(r, rr)
        g = max(g, rg)
        b = max(b, rb)

    return [_id, [r, g, b]]


def solve_all(games):
    solved = []
    for game in games:
        solved.append(game_solve(game))
    return solved


def cube_power(solution):
    [r, g, b] = solution
    return r * g * b


def possible_games_id_sum(games):
    possible_games = filter(lambda g: is_possible(12, 14, 13, g), games)
    sum = 0
    for p in possible_games:
        sum += p[0]
    return sum


def game_solution_powers_sum(games):
    sum = 0
    for solution in solve_all(games):
        [_id, s] = solution
        sum += cube_power(s)
    return sum


def main(filename="./day02/input"):
    all_games = parse_games(read_lines(filename))

    print(possible_games_id_sum(all_games))
    print(game_solution_powers_sum(all_games))


main("./day02/input")
