import os
import time
from colorama import Fore, Style
import sys
from heapq import heappush, heappop

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getStartAndEndPos(grid: list):
    startPos = None
    endPos = None

    startPos = (grid[0].index("."), 0)

    endPos = (grid[len(grid) - 1].index("."), len(grid) - 1)

    return startPos, endPos


def getTrailTiles(grid: list):
    trailTiles = set()

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != "#":
                trailTiles.add((x, y))

    return trailTiles


def getMaxDist(grid: list, start: tuple):
    dist = dict()

    nodes = getTrailTiles(grid)

    queue = list()

    for node in nodes:
        dist[node] = -1

    dist[start] = 0

    heappush(queue, (0, start[0], start[1], None))

    while queue:
        c, x, y, prevN = heappop(queue)

        cost = -c

        neighbors = []

        if grid[y][x] == ".":
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        elif grid[y][x] == "v":
            dirs = [(0, 1)]
        elif grid[y][x] == "^":
            dirs = [(0, -1)]
        elif grid[y][x] == "<":
            dirs = [(-1, 0)]
        elif grid[y][x] == ">":
            dirs = [(1, 0)]
        else:
            print("THIS SHOULD NEVER HAPPEN")

        for d in dirs:
            n = (x + d[0], y + d[1])

            if n in nodes and n != prevN:
                neighbors.append(n)

        for neigh in neighbors:
            alt = cost + 1
            if alt > dist[neigh]:
                dist[neigh] = alt

                heappush(queue, (-alt, neigh[0], neigh[1], (x, y)))

    return dist


def pt1():
    startPos, endPos = getStartAndEndPos(data)

    print(startPos)
    print(endPos)

    d = getMaxDist(data, startPos)

    return d[endPos]


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
