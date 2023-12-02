import re
from pathlib import Path

################################################################################


def count_cubes(game_set):
    red_re = r"(\d+) red"
    green_re = r"(\d+) green"
    blue_re = r"(\d+) blue"

    reds = re.findall(red_re, game_set)
    greens = re.findall(green_re, game_set)
    blues = re.findall(blue_re, game_set)

    red = 0
    green = 0
    blue = 0

    if len(reds) > 0:
        red = reds[0]
    if len(greens) > 0:
        green = greens[0]
    if len(blues) > 0:
        blue = blues[0]

    return int(red), int(green), int(blue)


def part1(data):
    red_max = 12
    green_max = 13
    blue_max = 14

    impossible_games = set()

    regex = r"Game \d+: "
    subst = ""

    for id, line in enumerate(data):
        id += 1

        line = re.sub(regex, subst, line)
        game_sets = line.split(";")

        for game_set in game_sets:
            red, green, blue = count_cubes(game_set)

            if red > red_max or green > green_max or blue > blue_max:
                impossible_games.add(id)

    possible_games = {x for x in range(1, len(data) + 1)}

    for x in impossible_games:
        possible_games.remove(x)

    return sum(possible_games)


################################################################################


def part2(data):
    power = []

    regex = r"Game \d+: "
    subst = ""

    for id, line in enumerate(data):
        id += 1

        line = re.sub(regex, subst, line)
        game_sets = line.split(";")

        red_min = 0
        green_min = 0
        blue_min = 0

        for game_set in game_sets:
            red, green, blue = count_cubes(game_set)

            red_min = max(red, red_min)
            green_min = max(green, green_min)
            blue_min = max(blue, blue_min)

        game_power = red_min * green_min * blue_min
        power.append(game_power)

    return sum(power)


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    return data


data = "src/day02/input.txt"
# data = "src/day02/example.txt"
# data = "src/day02/example2.txt"

print(part1(parse(data)))
print(part2(parse(data)))
