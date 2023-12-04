import re
from pathlib import Path

################################################################################


def get_wins(data):
    wins = {}
    regex = r"^Card\s*(\d+):\s*([^|]*)\|(.*)"

    for line in data:
        m = re.findall(regex, line)[0]

        id = int(m[0])
        winning = m[1].strip().replace("  ", " ").split(" ")
        owned = m[2].strip().replace("  ", " ").split(" ")

        for number in owned:
            if number in winning:
                wins[id] = wins.get(id, 0) + 1

    return wins


def part1(data):
    wins = get_wins(data)
    final = []

    for v in wins.values():
        res = 1

        while v - 1:
            res *= 2
            v -= 1

        final.append(res)

    return sum(final)


################################################################################


def part2(data):
    wins = get_wins(data)

    scratchcards = {x: 1 for x in range(1, len(data) + 1)}

    for current in range(1, len(data) + 1):
        if wins.get(current):
            for _ in range(scratchcards[current]):
                for new in range(current + 1, current + 1 + wins[current]):
                    scratchcards[new] += 1

    return sum(scratchcards.values())


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    return data


data = "src/day04/input.txt"
data = "src/day04/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))
