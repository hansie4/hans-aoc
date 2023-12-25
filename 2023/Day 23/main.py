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


def getSplits(nodes: set, start: tuple, end: tuple):
    splits = list()

    currentSplit = list()

    neighborsDict = dict()
    splitPoints = set()

    for node in nodes:
        neighbors = set()
        for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n = (node[0] + dir[0], node[1] + dir[1])

            if n in nodes:
                neighbors.add(n)
        neighborsDict[node] = neighbors
        if len(neighbors) > 2:
            splitPoints.add(node)

    splitPoints.add(start)
    splitPoints.add(end)

    for sp in splitPoints:
        dirs = neighborsDict[sp]

        for d in dirs:
            currentSplit = [sp, d]

            while True:
                currentNode = currentSplit[-1]

                if currentNode in splitPoints:
                    break

                neighbors = neighborsDict[currentNode]

                for n in neighbors:
                    if n not in currentSplit:
                        currentSplit.append(n)

            splits.append(currentSplit)

    edges = dict()

    for s in splits:
        edges[(s[0], s[-1])] = len(s) - 1

    return splitPoints, edges


LONGEST_DIST = 0


def getPaths(
    nodes: set(),
    edges: dict,
    start: tuple,
    end: tuple,
    currentNode: tuple,
    currentPath: list,
):
    newPath = currentPath.copy()
    newPath.append(currentNode)

    if currentNode == end:
        d = getPathLength(newPath, edges)
        global LONGEST_DIST

        if d > LONGEST_DIST:
            # print(d)
            LONGEST_DIST = d

    neighbors = list()
    for e in edges:
        if e[0] == currentNode and e[1] not in newPath:
            neighbors.append(e[1])

    for n in neighbors:
        getPaths(nodes, edges, start, end, n, newPath)


def getPathLength(path: list, edges: dict):
    c = 0
    for x in range(len(path) - 1):
        n1 = path[x]
        n2 = path[x + 1]

        d = edges[(n1, n2)]

        c = c + d

    return c


def pt1():
    startPos, endPos = getStartAndEndPos(data)

    d = getMaxDist(data, startPos)

    return d[endPos]


def pt2():
    sys.setrecursionlimit(10000)

    startPos, endPos = getStartAndEndPos(data)

    allNodes = getTrailTiles(data)

    nodes, edges = getSplits(allNodes, startPos, endPos)

    getPaths(nodes, edges, startPos, endPos, startPos, [])

    return LONGEST_DIST


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


test = """#S#####################
#OOOOOOO#########OOO###
#######O#########O#O###
###OOOOO#.>OOO###O#O###
###O#####.#O#O###O#O###
###O>...#.#O#OOOOO#OOO#
###O###.#.#O#########O#
###OOO#.#.#OOOOOOO#OOO#
#####O#.#.#######O#O###
#OOOOO#.#.#OOOOOOO#OOO#
#O#####.#.#O#########O#
#O#OOO#...#OOO###...>O#
#O#O#O#######O###.###O#
#OOO#O>.#...>O>.#.###O#
#####O#.#.###O#.#.###O#
#OOOOO#...#OOO#.#.#OOO#
#O#########O###.#.#O###
#OOO###OOO#OOO#...#O###
###O###O#O###O#####O###
#OOO#OOO#O#OOO>.#.>O###
#O###O###O#O###.#.#O###
#OOOOO###OOO###...#OOO#
#####################O#"""

x = 0
for j in test:
    for k in j:
        if k == "O":
            x += 1

print(x)
