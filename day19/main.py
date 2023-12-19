import re
from functools import reduce


def read_file(filename):
    with open(filename, "r") as f:
        return list(map(lambda s: s.split("\n"), f.read().split("\n\n")))


def parse_rule(line=""):
    if not ":" in line:
        return {"formula": False, "next": line}
    [rating, operand, value, next] = re.match(r"(.)(.)(\d+):(.*)", line).groups()
    return {
        "formula": True,
        "rating": rating,
        "operand": operand,
        "value": int(value),
        "next": next,
    }


def parse_workflow(acc={}, line=""):
    [name, l] = line.split("{")
    rules = l.split("}")[0]
    acc[name] = list(map(parse_rule, rules.split(",")))
    return acc


def parse_part(line=""):
    [x, m, a, s] = re.match(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", line).groups()
    part = {"x": int(x), "m": int(m), "a": int(a), "s": int(s)}
    return part


def process_workflow_rules(part, workflow):
    current_rule = workflow[0]
    for rule in workflow:
        if rule["formula"] == False:
            return rule["next"]

        if rule["operand"] == "<":
            if part[rule["rating"]] < rule["value"]:
                return rule["next"]
        else:
            if part[rule["rating"]] > rule["value"]:
                return rule["next"]

    raise ValueError("uh oh")


def is_accepted(part, workflows):
    current_step = "in"
    current_ = ""
    while current_step != "A" and current_step != "R":
        workflow = workflows[current_step]
        current_step = process_workflow_rules(part, workflow)

    return current_step == "A"


def main(filename="./day19/test"):
    [workflows, parts] = read_file(filename)
    workflows = reduce(parse_workflow, workflows, {})
    parts = list(map(parse_part, parts[:-1]))
    only_accepted = list(filter(lambda p: is_accepted(p, workflows), parts))
    rating_sum = list(map(lambda p: p["x"] + p["m"] + p["a"] + p["s"], only_accepted))
    sum = reduce(lambda a, b: a + b, rating_sum)
    print(sum)


main()
main("./day19/input")
