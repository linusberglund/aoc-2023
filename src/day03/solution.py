import re
from pathlib import Path

################################################################################


def get_symbols(data):
    regex = r"([^.\d])"
    symbols = {}

    for y, line in enumerate(data):
        for x, value in enumerate(line):
            if re.findall(regex, value):
                symbols[(x, y)] = value

    return symbols


def get_number_positions(data, symbols):
    max_x = len(data[0])
    max_y = len(data)

    initial_number_locations = set()

    for (x, y) in symbols.keys():
        for y_pos in range(x - 1, x + 2):
            for x_pos in range(y - 1, y + 2):
                if y_pos < 0 or y_pos > max_x or x_pos < 0 or x_pos > max_y:
                    continue

                if re.match(r"\d", data[x_pos][y_pos]):
                    initial_number_locations.add((x_pos, y_pos))

    return initial_number_locations


def get_numbers(data, positions):
    max_x = len(data[0])

    number_slices = set()
    numbers = []

    for x, y in positions:
        line = data[x]

        start_index = y
        end_index = y

        while True:
            if start_index < 0 or line[start_index].isdigit() is False:
                start_index += 1
                break
            start_index -= 1

        while True:
            if end_index >= max_x or line[end_index].isdigit() is False:
                end_index -= 1
                break
            end_index += 1

        number_slices.add((line, start_index, end_index + 1))

    for line, start_index, end_index in number_slices:
        numbers.append(int(line[start_index:end_index]))

    return numbers


def part1(data):
    symbols = get_symbols(data)
    positions = get_number_positions(data, symbols)
    numbers = get_numbers(data, positions)

    return sum(numbers)


################################################################################


def get_number_positions_with_symbol(data, symbols):
    max_x = len(data[0])
    max_y = len(data)

    initial_number_positions_with_symbol = set()

    for (x, y), symbol in symbols.items():
        for y_pos in range(x - 1, x + 2):
            for x_pos in range(y - 1, y + 2):
                if y_pos < 0 or y_pos > max_x or x_pos < 0 or x_pos > max_y:
                    continue

                if re.match(r"\d", data[x_pos][y_pos]):
                    initial_number_positions_with_symbol.add(((x_pos, y_pos), (x, y)))

    return initial_number_positions_with_symbol


def get_numbers_with_symbol(data, positions):
    max_x = len(data[0])

    number_slices = set()

    for (x, y), (symbol_x, symbol_y) in positions:
        line = data[x]

        start_index = y
        end_index = y

        while True:
            if start_index < 0 or line[start_index].isdigit() is False:
                start_index += 1
                break
            start_index -= 1

        while True:
            if end_index >= max_x or line[end_index].isdigit() is False:
                end_index -= 1
                break
            end_index += 1

        number_slices.add((line, start_index, end_index + 1, symbol_x, symbol_y))

    potential_numbers = dict(set())

    for line, start_index, end_index, symbol_x, symbol_y in number_slices:
        tmp = potential_numbers.get((symbol_x, symbol_y), set())
        tmp.add((line, start_index, end_index))
        potential_numbers[(symbol_x, symbol_y)] = tmp

    gear_sets = []

    for _, v in potential_numbers.items():
        if len(v) == 2:
            gear_sets.append(v)

    numbers = []

    for gear_set in gear_sets:
        line1, start_index1, end_index1 = gear_set.pop()
        line2, start_index2, end_index2 = gear_set.pop()

        number1 = int(line1[start_index1:end_index1])
        number2 = int(line2[start_index2:end_index2])

        numbers.append((number1, number2))

    return numbers


def part2(data):
    symbols = get_symbols(data)
    symbols = {k: v for k, v in symbols.items() if v == "*"}

    positions = get_number_positions_with_symbol(data, symbols)
    numbers = get_numbers_with_symbol(data, positions)

    gear_ratios = []

    for number_pair in numbers:
        gear_ratios.append(number_pair[0] * number_pair[1])

    return sum(gear_ratios)


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    return data


data = "src/day03/input.txt"
# data = "src/day03/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))
