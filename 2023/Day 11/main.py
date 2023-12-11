import os
import time
import math

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def performCosmicExpansion(galaxyMap: list):
    rowsWithNoGalaxies = list()
    columnsWithNoGalaxies = list()

    for y in range(len(galaxyMap)):
        if "#" not in galaxyMap[y]:
            rowsWithNoGalaxies.append(y)

    for x in range(len(galaxyMap[0])):
        noGalaxies = True
        for y in range(len(galaxyMap)):
            if galaxyMap[y][x] == "#":
                noGalaxies = False

        if noGalaxies:
            columnsWithNoGalaxies.append(x)

    # print(rowsWithNoGalaxies)
    # print(columnsWithNoGalaxies)

    newMap = list()

    for i in range(len(galaxyMap)):
        newMap.append(galaxyMap[i])

    columnsWithNoGalaxies.sort()

    for c in columnsWithNoGalaxies[::-1]:
        for r in range(len(newMap)):
            newMap[r] = newMap[r][:c] + "." + newMap[r][c:]

    emptyRow = "".join(["."] * len(newMap[0]))

    rowsWithNoGalaxies.sort()

    for r in rowsWithNoGalaxies[::-1]:
        newMap.insert(r, emptyRow)

    return newMap


def getGalaxyCords(galaxyMap: list):
    cords = set()

    for y in range(len(galaxyMap)):
        for x in range(len(galaxyMap[y])):
            if galaxyMap[y][x] == "#":
                cords.add((x, y))

    return cords


def printMap(galaxyMap: list):
    for x in galaxyMap:
        print("".join(x))


def getDist(g1: tuple, g2: tuple):
    x1 = g1[0]
    x2 = g2[0]
    y1 = g1[1]
    y2 = g2[1]

    return abs(x2 - x1) + abs(y2 - y1)


def getAllGalaxyCombos(galaxies: set):
    gList = list(galaxies)

    combos = set()

    for x in range(0, len(gList) - 1, 1):
        for y in range(x + 1, len(gList), 1):
            combos.add((gList[x], gList[y], getDist(gList[x], gList[y])))

    return combos


def getExpansionZones(galaxyMap: list):
    rowsWithNoGalaxies = list()
    columnsWithNoGalaxies = list()

    for y in range(len(galaxyMap)):
        if "#" not in galaxyMap[y]:
            rowsWithNoGalaxies.append(y)

    for x in range(len(galaxyMap[0])):
        noGalaxies = True
        for y in range(len(galaxyMap)):
            if galaxyMap[y][x] == "#":
                noGalaxies = False

        if noGalaxies:
            columnsWithNoGalaxies.append(x)

    # print(rowsWithNoGalaxies)
    # print(columnsWithNoGalaxies)

    return rowsWithNoGalaxies, columnsWithNoGalaxies


def applyExpansionToCords(
    galaxies: set, expansionAmount: int, rowsToExpand: list, columnsToExpand: list
):
    newGalaxies = set()

    rowsToExpand.sort()
    columnsToExpand.sort()

    for g in galaxies:
        # print(f"Expanding: {g}")
        gX = g[0]
        gY = g[1]

        timesToExpandRow = 0
        for rY in rowsToExpand:
            if gY > rY:
                timesToExpandRow += 1

        # print(timesToExpandRow)

        timesToExpandColumn = 0
        for rX in columnsToExpand:
            if gX > rX:
                timesToExpandColumn += 1

        # print(timesToExpandColumn)

        newGalaxies.add(
            (
                gX + (expansionAmount * timesToExpandColumn),
                gY + (expansionAmount * timesToExpandRow),
            )
        )

    return newGalaxies


def pt1():
    expandedGalaxyMap = performCosmicExpansion(data)

    # printMap(expandedGalaxyMap)

    galaxies = getGalaxyCords(expandedGalaxyMap)

    # print(galaxies)

    allGalaxyPairs = getAllGalaxyCombos(galaxies)

    dists = list(map(lambda x: x[2], allGalaxyPairs))

    ans = sum(dists)

    print(ans)
    return ans


def pt2():
    (
        rowsToExpand,
        columnsToExpand,
    ) = getExpansionZones(data)

    galaxies = getGalaxyCords(data)

    expandedGalaxies = applyExpansionToCords(
        galaxies, 999999, rowsToExpand, columnsToExpand
    )

    # print(expandedGalaxies)

    allGalaxyPairs = getAllGalaxyCombos(expandedGalaxies)

    dists = list(map(lambda x: x[2], allGalaxyPairs))

    ans = sum(dists)

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
