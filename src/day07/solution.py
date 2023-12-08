from copy import deepcopy
from functools import cmp_to_key
from pathlib import Path

################################################################################


def eval_hand(hand):
    v = {}
    score = []

    for x in hand:
        tmp = v.get(x, 0)
        tmp += 1
        v[x] = tmp

    for x, count in v.items():
        if count == 5:
            score.append(7)

        if count == 4:
            score.append(6)

        if count == 3:
            score.append(4)

            remaining = {k: v for k, v in v.items() if k is not x}
            for _, subcount in remaining.items():
                if subcount == 2:
                    score.append(5)

        if count == 2:
            score.append(2)

            remaining = {k: v for k, v in v.items() if k is not x}
            for _, subcount in remaining.items():
                if subcount == 2:
                    score.append(3)

        score.append(1)

    return max(score)


def compare_hands(hand_A, hand_B):
    hand1, bid1, strength1 = hand_A
    hand2, bid2, strength2 = hand_B

    if strength1 > strength2:
        return -1
    if strength2 > strength1:
        return 1

    for x, y in zip(hand1, hand2):
        match x:
            case "A":
                x = 14
            case "K":
                x = 13
            case "Q":
                x = 12
            case "J":
                x = 11
            case "T":
                x = 10
            case _:
                x = int(x)

        match y:
            case "A":
                y = 14
            case "K":
                y = 13
            case "Q":
                y = 12
            case "J":
                y = 11
            case "T":
                y = 10
            case _:
                y = int(y)

        if x > y:
            return -1
        if y > x:
            return 1

    return 0


def part1(data):
    hands = set()
    hands_strength = []
    hands_rank = []

    for line in data:
        hand, bid = line.split(" ")
        hands.add((hand, int(bid)))

    for hand, bid in hands:
        strength = eval_hand(hand)
        hands_strength.append((hand, bid, strength))

    hands_rank = deepcopy(hands_strength)
    hands_rank = sorted(hands_rank, key=cmp_to_key(compare_hands), reverse=True)

    result = 0

    for i, (hand, bid, strength) in enumerate(hands_rank):
        result += (i + 1) * bid

    return result


################################################################################


def eval_hand_2(hand):
    counts = {}
    score = []

    counts["J"] = 0

    for x in hand:
        tmp = counts.get(x, 0)
        tmp += 1
        counts[x] = tmp

    for x, count in counts.items():
        # Five of a kind = 7
        if count == 5:
            score.append(7)

        # Four of a kind = 6
        if count == 4:
            if counts["J"] >= 1:
                score.append(7)

            score.append(6)

        # Three of a kind = 4
        if count == 3 and x != "J":
            if counts["J"] == 2:
                score.append(7)

            if counts["J"] == 1:
                score.append(6)

            score.append(4)

            remaining = {k: v for k, v in counts.items() if k is not x}
            for _, subcount in remaining.items():
                if subcount == 2 or counts["J"] == 2:
                    # Full house = 5
                    score.append(5)

        # Two pair = 3
        if count == 2 and x != "J":
            score.append(2)

            if counts["J"] == 3:
                score.append(7)

            if counts["J"] == 2:
                score.append(6)

            if counts["J"] == 1:
                score.append(4)

            remaining = {k: v for k, v in counts.items() if k is not x}
            for _, subcount in remaining.items():
                if subcount == 2:
                    score.append(3)
                    if counts["J"] == 1:
                        score.append(5)

        # One pair = 1
        score.append(1)

        if counts["J"] == 3:
            score.append(6)

        if counts["J"] == 2:
            score.append(4)

        if counts["J"] == 1:
            score.append(2)

    return max(score)


def compare_hands_2(hand_A, hand_B):
    hand1, bid1, strength1 = hand_A
    hand2, bid2, strength2 = hand_B

    if strength1 > strength2:
        return -1
    if strength2 > strength1:
        return 1

    for x, y in zip(hand1, hand2):
        match x:
            case "A":
                x = 14
            case "K":
                x = 13
            case "Q":
                x = 12
            case "J":
                x = 1
            case "T":
                x = 10
            case _:
                x = int(x)

        match y:
            case "A":
                y = 14
            case "K":
                y = 13
            case "Q":
                y = 12
            case "J":
                y = 1
            case "T":
                y = 10
            case _:
                y = int(y)

        if x > y:
            return -1
        if y > x:
            return 1

    return 0


def part2(data):
    hands = set()
    hands_strength = []
    hands_rank = []

    for line in data:
        hand, bid = line.split(" ")
        hands.add((hand, int(bid)))

    for hand, bid in hands:
        strength = eval_hand_2(hand)
        hands_strength.append((hand, bid, strength))

    hands_rank = deepcopy(hands_strength)
    hands_rank = sorted(hands_rank, key=cmp_to_key(compare_hands_2), reverse=True)

    result = 0

    for i, (hand, bid, strength) in enumerate(hands_rank):
        result += (i + 1) * bid

    return result


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    return data


data = "src/day07/input.txt"
data = "src/day07/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))
