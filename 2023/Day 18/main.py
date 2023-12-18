import os
import time
from colorama import Fore, Style
import sys

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def createDataGrid():
    startPoint = (0, 0, "#ffffff")
    points = set()

    currentLocation = startPoint

    for l in data:
        t = l.split()
        direction = t[0]
        magnitude = int(t[1])
        color = t[2][1:-1]

        # print(f"{direction} | {magnitude} | {color}")
        if direction == "R":
            for p in range(
                currentLocation[0] + 1, currentLocation[0] + magnitude + 1, 1
            ):
                newPoint = (p, currentLocation[1], color, "R")
                points.add(newPoint)
                currentLocation = newPoint
        elif direction == "L":
            for p in range(
                currentLocation[0] - 1, currentLocation[0] - magnitude - 1, -1
            ):
                newPoint = (p, currentLocation[1], color, "L")
                points.add(newPoint)
                currentLocation = newPoint
        elif direction == "D":
            for p in range(
                currentLocation[1] + 1, currentLocation[1] + magnitude + 1, 1
            ):
                newPoint = (currentLocation[0], p, color, "D")
                points.add(newPoint)
                currentLocation = newPoint
        elif direction == "U":
            for p in range(
                currentLocation[1] - 1, currentLocation[1] - magnitude - 1, -1
            ):
                newPoint = (currentLocation[0], p, color, "U")
                points.add(newPoint)
                currentLocation = newPoint
        else:
            print("SERIOUS ISSUES!")

    return points


def getBounds(listOfPoints: set):
    minX = float("inf")
    minY = float("inf")
    maxX = float("-inf")
    maxY = float("-inf")

    for x in listOfPoints:
        if x[0] < minX:
            minX = x[0]
        if x[0] > maxX:
            maxX = x[0]
        if x[1] < minY:
            minY = x[1]
        if x[1] > maxY:
            maxY = x[1]

    return (minX, maxX), (minY, maxY)


def pointsToDict(points: set):
    d = dict()

    for x in points:
        d[(x[0], x[1])] = x

    return d


def toGrid(points: set):
    grid = list()
    pDict = pointsToDict(points)

    xBounds, yBounds = getBounds(points)
    xOffset = abs(xBounds[0])
    yOffset = abs(yBounds[0])

    for y in range(0, yBounds[1] + yOffset + 1, 1):
        newRow = []
        for x in range(0, xBounds[1] + xOffset + 1, 1):
            if (x - xOffset, y - yOffset) in pDict:
                newRow.append("#")
            else:
                newRow.append(".")
        grid.append(newRow)

    return grid


def floodFill(grid: list, x: int, y: int):
    if grid[y][x] != ".":
        return

    if grid[y][x] == "#":
        return

    grid[y][x] = "#"

    neighbors = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]

    for n in neighbors:
        if n[0] >= 0 and n[0] < len(grid[0]) and n[1] >= 0 and n[1] < len(grid):
            floodFill(grid, n[0], n[1])


def floodFillNonRecursive(grid: list, x: int, y: int):
    spacesToFill = set()
    spacesToFill.add((x, y))

    while len(spacesToFill) > 0:
        (a, b) = spacesToFill.pop()

        grid[b][a] = "#"

        neighbors = [
            (a - 1, b),
            (a + 1, b),
            (a, b - 1),
            (a, b + 1),
        ]

        for n in neighbors:
            if grid[n[1]][n[0]] == ".":
                spacesToFill.add((n[0], n[1]))


def pt1():
    trenchPoints = createDataGrid()

    grid = toGrid(trenchPoints)

    # for x in grid:
    #     print("".join(x))

    floodFillNonRecursive(grid, 100, 200)

    # for x in grid:
    #     print("".join(x))

    ans = 0

    for x in grid:
        for y in x:
            if y == "#":
                ans += 1

    return ans


def pt2():
    pass


print("Part 1 Answer:")
start_time = time.time()
print(Fore.GREEN + str(pt1()))
print(Style.RESET_ALL, end="")
print(f"It took {time.time() - start_time}s to get answer")
start_time = time.time()
print()
print("Part 2 Answer:")
print(Fore.GREEN + str(pt2()))
print(Style.RESET_ALL, end="")
print(f"It took {time.time() - start_time}s to get answer")
