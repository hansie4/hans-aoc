import os
import sys
import datetime
import math

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

    allSeedRanges = list()

    for x in range(0, len(seeds), 2):
        bottom = seeds[x]
        top = bottom + seeds[x + 1] - 1

        allSeedRanges.append((bottom, top))

    return allSeedRanges


def processSr(maps: dict, sr: list, granularity: int):
    min = sys.maxsize
    srFrom = None

    # print("Reading SR: ", sr)
    start = datetime.datetime.now()
    for s in range(sr[0], sr[1] + 1, granularity):
        t = s
        # print(s)
        for m in maps:
            t = getDest(maps[m], t)
            # print(m)
            # print(t)

        if t < min:
            min = t
            srFrom = sr
        # print(t)
    end = datetime.datetime.now()

    d = end - start
    # print(f"MIN FOUND: {min} from SR: {srFrom} | TIME TAKEN: {d}")
    return min, srFrom


def getSubRanges(r: tuple, p: int):
    diff = r[1] - r[0]
    inc = math.floor(diff / p)

    ranges = []

    for x in range(p * 2):
        if x == 0:
            ranges.append(r[0])
        elif x == (p * 2) - 1:
            ranges.append(r[1])
        else:
            if x % 2 == 0:
                val = ranges[x - 1] + 1
                ranges.append(val)
            else:
                val = ranges[x - 1] + inc
                ranges.append(val)

    ranges2 = list()

    for x in range(0, len(ranges), 2):
        n1 = ranges[x]
        n2 = ranges[x + 1]
        ranges2.append((n1, n2))

    # print(ranges2)
    return ranges2


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

    # print(maps)

    seeds = seedsToRanges(seeds)

    print(seeds)

    for x in maps:
        maps[x] = processMap(maps[x])

    # print(maps)
    # print(list(maps.keys()))

    bestMin = sys.maxsize
    bestSr = None

    gFactor = 100

    # First run:
    # for sr in seeds:
    #     min, x = processSr(maps, sr, gFactor)

    #     if min < bestMin:
    #         bestMin = min
    #         bestSr = x

    # Second run: [(3164519436, 3220959296), (3220959297, 3277399157), (3277399158, 3333839018), (3333839019, 3390278879), (3390278880, 3446718740), (3446718741, 3503158601), (3503158602, 3559598462), (3559598463, 3616038324), (3616038325, 3672478185), (3672478186, 3728918040)]
    # seeds = [
    #     (3164519436, 3220959296),
    #     (3220959297, 3277399157),
    #     (3277399158, 3333839018),
    #     (3333839019, 3390278879),
    #     (3390278880, 3446718740),
    #     (3446718741, 3503158601),
    #     (3503158602, 3559598462),
    #     (3559598463, 3616038324),
    #     (3616038325, 3672478185),
    #     (3672478186, 3728918040),
    # ]
    # for sr in seeds:
    #     min, x = processSr(maps, sr, gFactor)

    #     if min < bestMin:
    #         bestMin = min
    #         bestSr = x

    # Third run: [(3672478186, 3678122171), (3678122172, 3683766157), (3683766158, 3689410143), (3689410144, 3695054129), (3695054130, 3700698115), (3700698116, 3706342101), (3706342102, 3711986087) , (3711986088, 3717630073), (3717630074, 3723274059), (3723274060, 3728918040)]
    seeds = [
        (3672478186, 3678122171),
        (3678122172, 3683766157),
        (3683766158, 3689410143),
        (3689410144, 3695054129),
        (3695054130, 3700698115),
        (3700698116, 3706342101),
        (3706342102, 3711986087),
        (3711986088, 3717630073),
        (3717630074, 3723274059),
        (3723274060, 3728918040),
    ]
    for sr in seeds:
        min, x = processSr(maps, sr, gFactor)

        if min < bestMin:
            bestMin = min
            bestSr = x

    print(f"Best Min = {bestMin} from {bestSr} GRANULARITY = {gFactor}")


def pt3():
    seeds, maps = getInputs(data)

    # print(maps)

    seeds = seedsToRanges(seeds)

    # print(seeds)

    for x in maps:
        maps[x] = processMap(maps[x])

    # print(maps)
    # print(list(maps.keys()))

    # -------------------------------------------------------------------

    rFactor = 6
    bFactor = 8

    newSeeds = seeds

    bestMin = sys.maxsize
    bestSr = None

    for run in range(rFactor):
        gFactor = int(math.pow(bFactor, ((rFactor - 1) - run)))
        print(f"Run: {run} with gFactor: {gFactor}")

        for sr in newSeeds:
            min, x = processSr(maps, sr, gFactor)

            if min < bestMin:
                bestMin = min
                bestSr = x

        print(f"Best Min = {bestMin} from {bestSr} GRANULARITY = {gFactor}")
        newSeeds = getSubRanges(bestSr, bFactor)

    print(bestMin)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
# pt2()
pt3()
