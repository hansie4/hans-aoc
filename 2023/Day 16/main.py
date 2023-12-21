import os
import time
from colorama import Fore, Style
from collections import deque

from numpy import isin

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()

DIRECTION_MAP = {
    (-1, 0): {
        "/": [(0, 1)],
        "\\": [(0, -1)],
        "-": [(-1, 0)],
        "|": [(0, -1), (0, 1)],
        ".": [(-1, 0)],
    },
    (1, 0): {
        "/": [(0, -1)],
        "\\": [(0, 1)],
        "-": [(1, 0)],
        "|": [(0, -1), (0, 1)],
        ".": [(1, 0)],
    },
    (0, -1): {
        "/": [(1, 0)],
        "\\": [(-1, 0)],
        "-": [(1, 0), (-1, 0)],
        "|": [(0, -1)],
        ".": [(0, -1)],
    },
    (0, 1): {
        "/": [(-1, 0)],
        "\\": [(1, 0)],
        "-": [(1, 0), (-1, 0)],
        "|": [(0, 1)],
        ".": [(0, 1)],
    },
}


def getInitEnergizedGrid(grid: list):
    energized = list()

    for y in range(len(grid)):
        energized.append([False] * len(grid[y]))

    return energized


def isInBounds(node: tuple, maxX: int, maxY: int):
    x = node[0]
    y = node[1]

    if x < 0 or y < 0 or x > maxX or y > maxY:
        return False

    return True


def getNumEnergized(grid: list, start: tuple):
    visited = set()

    queue = deque()
    queue.append(start)

    while queue:
        x, y, dX, dY = queue.popleft()

        newX = x + dX
        newY = y + dY

        if isInBounds((newX, newY), len(grid[0]) - 1, len(grid) - 1):
            nextChar = grid[newY][newX]

            nextDirs = DIRECTION_MAP[(dX, dY)][nextChar]

            for dir in nextDirs:
                if (newX, newY, dir[0], dir[1]) not in visited:
                    visited.add((newX, newY, dir[0], dir[1]))
                    queue.append((newX, newY, dir[0], dir[1]))

    # print(visited)

    return len(set(map(lambda x: (x[0], x[1]), visited)))


def getAllPossibleStarts(grid: list):
    starts = set()

    for x in range(len(grid[0])):
        starts.add((x, -1, 0, 1))
        starts.add((x, len(grid), 0, -1))

    for y in range(len(grid)):
        starts.add((-1, y, 1, 0))
        starts.add((len(grid[0]), y, -1, 0))

    return starts


def pt1():
    start = (-1, 0, 1, 0)
    energized = getNumEnergized(data, start)
    return energized


def pt2():
    ans = -1

    allPossibleStarts = getAllPossibleStarts(data)

    for start in allPossibleStarts:
        energized = getNumEnergized(data, start)

        if energized > ans:
            ans = energized

    return ans


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
