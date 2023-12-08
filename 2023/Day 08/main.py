import os
import time
import math

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def findInterval(
    lookup: dict,
    instructions: list,
    startLocation: str,
    endLocations: set,
    matchFactor: int,
):
    currentLocation = startLocation
    currentInstruction = 0

    moves = 0
    last = 0

    diff = 0

    lastMatched = 0

    while lastMatched < matchFactor:
        move = instructions[currentInstruction]

        if move == "L":
            currentLocation = lookup[currentLocation]["left"]
        else:
            currentLocation = lookup[currentLocation]["right"]

        moves += 1

        currentInstruction += 1

        if currentInstruction == len(instructions):
            currentInstruction = 0

        if currentLocation in endLocations:
            if moves - last == diff:
                lastMatched += 1

            diff = moves - last
            # print(diff)
            last = moves

    return diff


def pt1():
    instructions = data[0]

    unparsedRows = data[2:]
    # print(unparsedRows)

    lookup = dict()
    for x in unparsedRows:
        t = x.split(" = ")
        lookup[t[0]] = dict()
        tt = t[1][1:-1].split(", ")
        lookup[t[0]]["left"] = tt[0]
        lookup[t[0]]["right"] = tt[1]

    # print(lookup)

    currentLocation = "AAA"
    currentInstruction = 0

    moves = 0

    while currentLocation != "ZZZ":
        move = instructions[currentInstruction]

        if move == "L":
            currentLocation = lookup[currentLocation]["left"]
        else:
            currentLocation = lookup[currentLocation]["right"]

        moves += 1

        currentInstruction += 1

        if currentInstruction == len(instructions):
            currentInstruction = 0

    print(moves)


def pt2():
    instructions = data[0]

    unparsedRows = data[2:]
    # print(unparsedRows)

    starts = set()
    ends = set()

    lookup = dict()
    for x in unparsedRows:
        t = x.split(" = ")
        lookup[t[0]] = dict()
        tt = t[1][1:-1].split(", ")
        lookup[t[0]]["left"] = tt[0]
        lookup[t[0]]["right"] = tt[1]

        if t[0].endswith("A"):
            starts.add(t[0])
        elif t[0].endswith("Z"):
            ends.add(t[0])

    # print(starts)
    # print(ends)

    ghostLocations = list(starts)

    vals = list()

    for x in ghostLocations:
        i = findInterval(lookup, instructions, x, ends, 1)
        # print(i)
        vals.append(i)

    # print(vals)
    ans = math.lcm(*vals)

    print(ans)
    return ans


print("Part 1 Answer:")
start_time = time.time()
pt1()
print(f"It took {time.time() - start_time}s to get answer")
start_time = time.time()
print("Part 2 Answer:")
pt2()
print(f"It took {time.time() - start_time}s to get answer")
