import re
import sys
from pathlib import Path
from pprint import pp

################################################################################


def gen_map(data, i, mapping):
    for x in data[i + 1 :]:
        if not x:
            break
        dest, start, ran = x.split(" ")
        dest, start, ran = int(dest), int(start), int(ran)
        mapping[start] = (dest, ran)

    return mapping


def check_map(mapping, seed):
    number = seed

    for entry in mapping.items():
        source, (dest, ran) = entry

        if number >= source and number < source + ran:
            number += dest - source
            break

    return number


def part1(data):
    data = [line.replace("-", "_") for line in data]

    seeds = data[0]
    seeds = seeds.replace("seeds: ", "").split(" ")
    seeds = [int(x) for x in seeds]

    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}

    for i, line in enumerate(data):
        line = line.replace(" map:", "")

        match line:
            case "seed_to_soil":
                gen_map(data, i, seed_to_soil)
            case "soil_to_fertilizer":
                gen_map(data, i, soil_to_fertilizer)
            case "fertilizer_to_water":
                gen_map(data, i, fertilizer_to_water)
            case "water_to_light":
                gen_map(data, i, water_to_light)
            case "light_to_temperature":
                gen_map(data, i, light_to_temperature)
            case "temperature_to_humidity":
                gen_map(data, i, temperature_to_humidity)
            case "humidity_to_location":
                gen_map(data, i, humidity_to_location)

    results = []

    for seed in seeds:
        current = seed

        current = check_map(seed_to_soil, current)
        current = check_map(soil_to_fertilizer, current)
        current = check_map(fertilizer_to_water, current)
        current = check_map(water_to_light, current)
        current = check_map(light_to_temperature, current)
        current = check_map(temperature_to_humidity, current)
        current = check_map(humidity_to_location, current)

        results.append(current)

    return min(results)


################################################################################


def gen_map_part2(data, i, mapping):
    mapping_rev = {}

    for x in data[i + 1 :]:
        if not x:
            break

        dest, start, ran = [int(n) for n in x.split(" ")]

        mapping[start] = (dest, ran)
        mapping_rev[dest] = (start, ran)

    return mapping, mapping_rev


def part2(data):
    data = [line.replace("-", "_") for line in data]

    seeds = data[0]
    seeds = seeds.replace("seeds: ", "").split(" ")
    seeds = [int(x) for x in seeds]

    real_seeds = []

    for i, x in enumerate(seeds):
        if not i % 2:
            real_seeds.append((x, seeds[i + 1]))

    # pp(real_seeds)

    soil = {}
    fertilizer = {}
    water = {}
    light = {}
    temperature = {}
    humidity = {}
    location = {}

    soil_rev = {}
    fertilizer_rev = {}
    water_rev = {}
    light_rev = {}
    temperature_rev = {}
    humidity_rev = {}
    location_rev = {}

    for i, line in enumerate(data):
        line = line.replace(" map:", "")

        match line:
            case "seed_to_soil":
                soil, soil_rev = gen_map_part2(data, i, soil)
            case "soil_to_fertilizer":
                fertilizer, fertilizer_rev = gen_map_part2(data, i, soil)
            case "fertilizer_to_water":
                water, water_rev = gen_map_part2(data, i, soil)
            case "water_to_light":
                light, light_rev = gen_map_part2(data, i, soil)
            case "light_to_temperature":
                temperature, temperature_rev = gen_map_part2(data, i, soil)
            case "temperature_to_humidity":
                humidity, humidity_rev = gen_map_part2(data, i, soil)
            case "humidity_to_location":
                location, location_rev = gen_map_part2(data, i, soil)\

    lowest_location = None

    all_final_locations = []

    location_dests = sorted(location_rev.keys())

    for dest in location_dests:
        start, ran = location_rev[dest]

        for i in range(dest, dest + ran + 1):
            pass

    return lowest_location



################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()

    # data = [(x, int(y)) for x, y in data]
    # data = [[[int(x) for x in y] for y in line] for line in data]
    # data = [[int(x) for x in line] for line in data]
    # data = [[x for x in line] for line in data]
    # data = [[x.split(",") for x in line] for line in data]
    # data = [line.split(" ") for line in data]
    # data = [line.split(",") for line in data]
    # data = [line.strip("\n") for line in data]
    # data = [x.split(" -> ") for x in data]
    # data = [x[0] for x in data]

    return data


data = "src/day05/input.txt"
data = "src/day05/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))
