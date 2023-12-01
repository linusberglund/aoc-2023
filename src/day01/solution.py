import re
from pathlib import Path

################################################################################


def part1(data):
    cal = []

    for line in data:
        first = None
        last = None

        for c in line:
            if c.isdigit():
                if not first:
                    first = c
                    last = c
                else:
                    last = c

        cal.append(int(first + last))

    return sum(cal)


################################################################################


def get_num(text):
    match text:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case _:
            return None


def part2(data):
    cal = []

    regex = r"^(one|two|three|four|five|six|seven|eight|nine)"

    for line in data:
        first = None
        last = None

        while line:
            m = re.findall(regex, line)

            if first is None:
                if line[0].isdigit():
                    first = line[0]
                    last = line[0]
                if m:
                    first = get_num(m[0])
                    last = get_num(m[0])
            else:
                if line[0].isdigit():
                    first = line[0]
                if m:
                    first = get_num(m[0])

            line = line[1:]

        cal.append(int(last + first))

    return sum(cal)


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    return data


data = "src/day01/input.txt"
# data = "src/day01/example.txt"
# data = "src/day01/example2.txt"

print(part1(parse(data)))
print(part2(parse(data)))
