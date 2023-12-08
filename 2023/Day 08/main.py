import os
import time

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


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
    ghostsAtEnd = [False] * len(ghostLocations)

    currentInstruction = 0
    steps = 0

    while not all(ghostsAtEnd):
        move = instructions[currentInstruction]

        for gi in range(len(ghostLocations)):
            currentGhostLocation = ghostLocations[gi]

            if move == "L":
                ghostLocations[gi] = lookup[currentGhostLocation]["left"]
            else:
                ghostLocations[gi] = lookup[currentGhostLocation]["right"]

            ghostsAtEnd[gi] = ghostLocations[gi] in ends

        steps += 1
        currentInstruction += 1

        if currentInstruction == len(instructions):
            currentInstruction = 0

        print(ghostsAtEnd)

    print(steps)


print("Part 1 Answer:")
start_time = time.time()
# pt1()
print(f"It took {time.time() - start_time}s to get answer")
start_time = time.time()
print("Part 2 Answer:")
pt2()
print(f"It took {time.time() - start_time}s to get answer")
