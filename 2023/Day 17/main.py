import os
import time
from colorama import Fore, Style
from heapq import heappop, heappush
import sys

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def readInDataGrid(dataGrid: list):
    grid = list()

    for y in range(len(dataGrid)):
        row = list()
        for x in range(len(dataGrid[y])):
            row.append(int(dataGrid[y][x]))
        grid.append(row)

    return grid


def getMinHeatLoss(grid: list, start: tuple, end: tuple):
    visited = set()

    queue = [(0, start[0], start[1], (0, 0), 0)]

    while queue:
        cost, x, y, dir, numInRow = heappop(queue)

        if (x, y) == end:
            return cost

        if (x, y, dir, numInRow) in visited:
            continue

        visited.add((x, y, dir, numInRow))

        # Getting possible next nodes
        nextDirs = {(1, 0), (-1, 0), (0, 1), (0, -1)}

        if numInRow < 3 and dir != (0, 0):
            nX = x + dir[0]
            nY = y + dir[1]

            if 0 <= nX < len(grid[0]) and 0 <= nY < len(grid):
                heappush(queue, (cost + grid[nY][nX], nX, nY, dir, numInRow + 1))

        for d in nextDirs:
            if d != dir and d != (0 - dir[0], 0 - dir[1]):
                nX = x + d[0]
                nY = y + d[1]

                if 0 <= nX < len(grid[0]) and 0 <= nY < len(grid):
                    heappush(queue, (cost + grid[nY][nX], nX, nY, d, 1))

    return visited


def getMinHeatLoss2(grid: list, start: tuple, end: tuple):
    visited = set()

    queue = [(0, start[0], start[1], (0, 0), 0)]

    while queue:
        cost, x, y, dir, numInRow = heappop(queue)

        if (x, y) == end and numInRow >= 4:
            return cost

        if (x, y, dir, numInRow) in visited:
            continue

        visited.add((x, y, dir, numInRow))

        # Getting possible next nodes
        nextDirs = {(1, 0), (-1, 0), (0, 1), (0, -1)}

        if numInRow < 10 and dir != (0, 0):
            nX = x + dir[0]
            nY = y + dir[1]

            if 0 <= nX < len(grid[0]) and 0 <= nY < len(grid):
                heappush(queue, (cost + grid[nY][nX], nX, nY, dir, numInRow + 1))

        if numInRow >= 4 or dir == (0, 0):
            for d in nextDirs:
                if d != dir and d != (0 - dir[0], 0 - dir[1]):
                    nX = x + d[0]
                    nY = y + d[1]

                    if 0 <= nX < len(grid[0]) and 0 <= nY < len(grid):
                        heappush(queue, (cost + grid[nY][nX], nX, nY, d, 1))

    return visited


def pt1():
    grid = readInDataGrid(data)

    ans = getMinHeatLoss(grid, (0, 0), (len(grid[0]) - 1, len(grid) - 1))

    return ans


def pt2():
    grid = readInDataGrid(data)

    ans = getMinHeatLoss2(grid, (0, 0), (len(grid[0]) - 1, len(grid) - 1))

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
