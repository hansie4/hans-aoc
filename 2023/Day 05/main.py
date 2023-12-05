import os
import sys

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getInputs(info: list):
    seeds = list(map(lambda x: int(x), info[0].split(": ", 2)[1].split()))

    maps = dict()

    encodedMaps = list()

    mapText = info[2:]
    mapText.append("")

    newChunk = list()

    for x in mapText:
        if x == "":
            encodedMaps.append(newChunk)
            newChunk = list()
        else:
            newChunk.append(x)

    # print(encodedMaps)

    for x in encodedMaps:
        temp = x[0][:-5].split("-to-")
        k = (temp[0], temp[1])
        # print(k)
        instructions = list()
        for y in x[1:]:
            t = y.split()
            instructions.append(list(map(lambda z: int(z), t)))

        # print(instructions)
        maps[k] = instructions

    return seeds, maps


def processMap(m: list):
    sourceToDest = dict()

    for x in m:
        # print(f"({x[1]}, {x[1] + x[2] - 1}) -> {x[0]}+")
        sourceToDest[(x[1], x[1] + x[2] - 1)] = x[0]

    return sourceToDest


def isWithinRange(r: tuple, k: int):
    # print(r)
    return k >= r[0] and k <= r[1]


def getDest(m: dict, val: int):
    for x in m.keys():
        if isWithinRange(x, val):
            # print("HERE")
            return m[x] + (val - x[0])

    return val


def seedsToRanges(seeds: list):
    # print(seeds)

    allSeeds = set()

    for x in range(0, len(seeds), 2):
        bottom = seeds[x]
        top = bottom + seeds[x + 1]

        # print(f"{bottom} - {top}")
        for y in range(bottom, top):
            allSeeds.add(y)

    # print(list(allSeeds))
    # print(len(allSeeds))

    return allSeeds


def pt1():
    seeds, maps = getInputs(data)

    # print(seeds)
    # print(maps)

    for x in maps:
        maps[x] = processMap(maps[x])

    # print(maps)
    # print(list(maps.keys()))

    min = sys.maxsize

    for s in seeds:
        t = s
        # print(s)
        for m in maps:
            t = getDest(maps[m], t)
            # print(m)
            # print(t)

        if t < min:
            min = t
        # print(t)

    print(min)
    return min


def pt2():
    seeds, maps = getInputs(data)

    # print(seeds)
    # print(maps)

    seeds = seedsToRanges(seeds)

    for x in maps:
        maps[x] = processMap(maps[x])

    # print(maps)
    # print(list(maps.keys()))

    min = sys.maxsize

    for s in seeds:
        t = s
        # print(s)
        for m in maps:
            t = getDest(maps[m], t)
            # print(m)
            # print(t)

        if t < min:
            min = t
        # print(t)

    print(min)
    return min


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
