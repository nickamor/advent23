import re
from functools import reduce


def read_file(filename):
    def parse_plan_step(line=""):
        [direction, distance, color] = re.match(r"(.) (\d+) \((.*)\)", line).groups()
        return (direction, int(distance), color)

    with open(filename, "r") as f:
        return list(map(parse_plan_step, f.read().split("\n")[:-1]))


def dig(coords=(0, 0), dig_map=[[""]]):
    new_map = dig_map.copy()
    (x, y) = coords
    new_map[y][x] = "#"
    return new_map


def create_map(width, height):
    dig_map = []
    for h in range(height):
        dig_map.append([])
        for w in range(width):
            dig_map[h].append(".")

    return dig_map


dig_plan = read_file("./day18/test")
print(dig_plan)

width = reduce(lambda acc, curr: acc + curr[1] if curr[0] == "R" else acc, dig_plan, 1)
height = reduce(lambda acc, curr: acc + curr[1] if curr[0] == "D" else acc, dig_plan, 1)
dig_map = create_map(width, height)
current_coord = (0, 0)
dig_map = dig(current_coord, dig_map)
for step in dig_plan:
    (direction, dist, _color) = step
    for i in range(dist):
        (x, y) = current_coord
        if direction == "U":
            y -= 1
        if direction == "D":
            y += 1
        if direction == "L":
            x -= 1
        if direction == "R":
            x += 1
        current_coord = (x, y)
        dig_map = dig(current_coord, dig_map)
final_map = reduce(lambda acc, curr: , dig_map, "")
print()
