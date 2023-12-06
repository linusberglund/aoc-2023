from pathlib import Path

################################################################################


def part1(data):
    times = []

    for x in data[0].replace("Time:", "").replace("  ", " ").split(" "):
        if x:
            times.append(int(x))

    distances = []

    for x in data[1].replace("Distance:", "").replace("  ", " ").split(" "):
        if x:
            distances.append(int(x))

    results = {}

    for time, dist in zip(times, distances):
        for i in range(time):
            if i * (time - i) > dist:
                tmp = results.get(time, [])
                tmp.append(i * (time - i))
                results[time] = tmp

    final_results = []

    for res in results.values():
        final_results.append(len(res))

    final_sum = 1

    for x in final_results:
        final_sum *= x

    return final_sum


################################################################################


def part2(data):
    time = int(data[0].replace("Time:", "").replace(" ", ""))
    distance = int(data[1].replace("Distance:", "").replace(" ", ""))

    results = []

    for i in range(time):
        if i * (time - i) > distance:
            results.append(i * (time - i))

    return len(results)


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    return data


data = "src/day06/input.txt"
data = "src/day06/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))
