import math
from pathlib import Path

################################################################################


def step_sequence(nodes, sequence, current, steps):
    for c in sequence:
        steps += 1
        match c:
            case "L":
                current = nodes[current][0]
            case "R":
                current = nodes[current][1]

    return current, steps


def part1(data):
    instructions = data[0]
    nodes = dict()

    for line in data[2:]:
        line = (
            line.replace(" = ", " ")
            .replace("(", "")
            .replace(", ", " ")
            .replace(")", "")
        )
        line = line.split(" ")

        node = line[0]
        left = line[1]
        right = line[2]

        nodes[node] = (left, right)

    current = "AAA"
    steps = 0

    while current != "ZZZ":
        current, steps = step_sequence(nodes, instructions, current, steps)

    return steps


################################################################################


def part2(data):
    instructions = data[0]
    nodes = {}

    for line in data[2:]:
        line = (
            line.replace(" = ", " ")
            .replace("(", "")
            .replace(", ", " ")
            .replace(")", "")
        )
        line = line.split(" ")

        node = line[0]
        left = line[1]
        right = line[2]

        nodes[node] = (left, right)

    starting_nodes = []
    end_nodes = []

    for node in nodes.keys():
        match node[2]:
            case "A":
                starting_nodes.append(node)
            case "Z":
                end_nodes.append(node)

    currents = starting_nodes
    steps = 0

    steps_until_Z = [None for _ in range(len(starting_nodes))]

    while True:
        for instruction in instructions:
            for i, current in enumerate(currents):
                if steps_until_Z[i] is None and current[2] == "Z":
                    steps_until_Z[i] = steps

            steps_not_found = [x for x in steps_until_Z if x is None]

            if len(steps_not_found) == 0:
                return math.lcm(*steps_until_Z)

            for i, current in enumerate(currents):
                match instruction:
                    case "L":
                        currents[i] = nodes[current][0]
                    case "R":
                        currents[i] = nodes[current][1]

            steps += 1


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    return data


data = "src/day08/input.txt"
data = "src/day08/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))
