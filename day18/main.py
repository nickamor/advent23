import array
from ctypes import Array
import re
from functools import reduce


def read_file(filename):
    def parse_plan_step(line=""):
        [direction, distance, color] = re.match(r"(.) (\d+) \((.*)\)", line).groups()
        return (direction, int(distance), color)

    with open(filename, "r") as f:
        return list(map(parse_plan_step, f.read().split("\n")[:-1]))


def dig_hole(coords, dig_map):
    (x, y) = coords

    (rows, cols) = dig_map.size
    if y + 1 > cols or x + 1 > rows:
        dig_map = dig_map.resize((max(x + 1, rows), max(y + 1, cols)))

    dig_map.data[y][x] = "#"
    return dig_map


def create_map():
    class Grid:
        def __init__(self, data=[], size=(0,0)) -> None:
            self.data = data
            self.size = size

        def resize(self, new_size):
            (columns, rows) = self.size
            (new_columns, new_rows)=new_size

            new_data = [['.' for j in range(new_columns)] for i in range(new_rows)]

            for i in range(new_rows):
                for j in range(new_columns):
                    new_data[i][j] = self.data[i][j] if i < rows and j < columns else '.'

            # self.data=new_data
            # self.size=new_size

            return Grid(new_data, new_size)

    return Grid()


dig_plan = read_file("./day18/test")

# width = reduce(lambda acc, curr: acc + curr[1] if curr[0] == "R" else acc, dig_plan, 1)
# height = reduce(lambda acc, curr: acc + curr[1] if curr[0] == "D" else acc, dig_plan, 1)
dig_map = create_map()

current_coord = (0, 0)
dig_map = dig_hole(current_coord, dig_map)

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
        dig_map = dig_hole(current_coord, dig_map)

final_map = reduce(lambda acc, curr: acc + str.join("", curr) + "\n", dig_map.data, "")
print(final_map)
