import os
import time

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def findStart(pipeMap: list):
    for y in range(len(pipeMap)):
        for x in range(len(pipeMap[y])):
            if pipeMap[y][x] == "S":
                return (x, y)


def canConnectFromRight(pipeType: str):
    return pipeType == "L" or pipeType == "-" or pipeType == "F" or pipeType == "S"


def canConnectFromLeft(pipeType: str):
    return pipeType == "7" or pipeType == "-" or pipeType == "J" or pipeType == "S"


def canConnectFromTop(pipeType: str):
    return pipeType == "|" or pipeType == "L" or pipeType == "J" or pipeType == "S"


def canConnectFromBottom(pipeType: str):
    return pipeType == "|" or pipeType == "F" or pipeType == "7" or pipeType == "S"


def getNextPossiblePipes(pipeMap: list, currentPipe: tuple, alreadyVisited: set):
    nextPipes = list()

    cp = pipeMap[currentPipe[1]][currentPipe[0]]

    instructionsToExecute = set()
    # 1 = Top
    # 2 = Bottom
    # 3 = Left
    # 4 = Right

    if cp == "S":
        instructionsToExecute.add(1)
        instructionsToExecute.add(2)
        instructionsToExecute.add(3)
        instructionsToExecute.add(4)
    elif cp == "7":
        instructionsToExecute.add(2)
        instructionsToExecute.add(3)
    elif cp == "J":
        instructionsToExecute.add(1)
        instructionsToExecute.add(3)
    elif cp == "L":
        instructionsToExecute.add(1)
        instructionsToExecute.add(4)
    elif cp == "F":
        instructionsToExecute.add(2)
        instructionsToExecute.add(4)
    elif cp == "|":
        instructionsToExecute.add(1)
        instructionsToExecute.add(2)
    elif cp == "-":
        instructionsToExecute.add(3)
        instructionsToExecute.add(4)

    if 1 in instructionsToExecute:
        # Top pipe
        if currentPipe[1] != 0:
            nextPipeCords = (currentPipe[0], currentPipe[1] - 1)
            if nextPipeCords not in alreadyVisited:
                nextPipeType = pipeMap[nextPipeCords[1]][nextPipeCords[0]]
                if canConnectFromBottom(nextPipeType):
                    nextPipes.append(nextPipeCords)
    if 2 in instructionsToExecute:
        # Bottom pipe
        if currentPipe[1] != len(pipeMap) - 1:
            nextPipeCords = (currentPipe[0], currentPipe[1] + 1)
            if nextPipeCords not in alreadyVisited:
                nextPipeType = pipeMap[nextPipeCords[1]][nextPipeCords[0]]
                if canConnectFromTop(nextPipeType):
                    nextPipes.append(nextPipeCords)
    if 3 in instructionsToExecute:
        # Left pipe
        if currentPipe[0] != 0:
            nextPipeCords = (currentPipe[0] - 1, currentPipe[1])
            if nextPipeCords not in alreadyVisited:
                nextPipeType = pipeMap[nextPipeCords[1]][nextPipeCords[0]]
                if canConnectFromRight(nextPipeType):
                    nextPipes.append(nextPipeCords)
    if 4 in instructionsToExecute:
        # Right pipe
        if currentPipe[0] != len(pipeMap[currentPipe[1]]) - 1:
            nextPipeCords = (currentPipe[0] + 1, currentPipe[1])
            if nextPipeCords not in alreadyVisited:
                nextPipeType = pipeMap[nextPipeCords[1]][nextPipeCords[0]]
                if canConnectFromLeft(nextPipeType):
                    nextPipes.append(nextPipeCords)

    return nextPipes


def findLoop(pipeMap: list):
    visited = set()

    currentPipe = findStart(pipeMap)

    # print(f"Starting at {currentPipe}")

    while True:
        visited.add(currentPipe)

        nextPipes = getNextPossiblePipes(pipeMap, currentPipe, visited)

        # print(nextPipes)

        if len(nextPipes) == 0:
            break

        currentPipe = nextPipes[0]

    return visited


def printLoop(loop: set, pipeMap: list):
    for y in range(len(pipeMap)):
        for x in range(len(pipeMap[y])):
            char = pipeMap[y][x]
            if (x, y) in loop:
                if char == "-":
                    print("━", end="")
                elif char == "|":
                    print("┃", end="")
                elif char == "J":
                    print("┛", end="")
                elif char == "7":
                    print("┓", end="")
                elif char == "L":
                    print("┗", end="")
                elif char == "F":
                    print("┏", end="")
                else:
                    print(char, end="")
            else:
                if char == "*":
                    print("▉", end="")
                else:
                    print("╳", end="")
        print()


def removeBadPipes(pipeMap: list, validPipes: set):
    for y in range(len(pipeMap)):
        for x in range(len(pipeMap[y])):
            if (x, y) not in validPipes:
                pipeMap[y] = pipeMap[y][:x] + "." + pipeMap[y][x + 1 :]


def replaceSWith(pipeMap: list):
    sLoc = findStart(pipeMap)

    nextPipes = getNextPossiblePipes(pipeMap, sLoc, set())

    top = (sLoc[0], sLoc[1] - 1) in nextPipes
    bottom = (sLoc[0], sLoc[1] + 1) in nextPipes
    left = (sLoc[0] - 1, sLoc[1]) in nextPipes
    right = (sLoc[0] + 1, sLoc[1]) in nextPipes

    newVal = ""

    if top and bottom:
        newVal = "|"
    elif top and left:
        newVal = "J"
    elif top and right:
        newVal = "L"
    elif bottom and left:
        newVal = "7"
    elif bottom and right:
        newVal = "F"
    elif left and right:
        newVal = "-"

    return newVal


def uniqueEdgesLeft(pipeMap: list, point: tuple):
    uniqueEdges = 0

    lastEdgeStart = None

    for x in range(point[0], -1, -1):
        v = pipeMap[point[1]][x]

        if v in ["7", "J"]:
            lastEdgeStart = v

        if v == "L" and lastEdgeStart == "7":
            # print("A")
            uniqueEdges += 1
        elif v == "L" and lastEdgeStart == "J":
            # print("B")
            uniqueEdges += 2
        elif v == "F" and lastEdgeStart == "7":
            # print("C")
            uniqueEdges += 2
        elif v == "F" and lastEdgeStart == "J":
            # print("D")
            uniqueEdges += 1
        elif v == "|":
            # print("E")
            uniqueEdges += 1

    return uniqueEdges


def uniqueEdgesRight(pipeMap: list, point: tuple):
    uniqueEdges = 0

    lastEdgeStart = None

    for x in range(point[0], len(pipeMap[point[1]]), 1):
        v = pipeMap[point[1]][x]

        if v in ["L", "F"]:
            lastEdgeStart = v

        if v == "7" and lastEdgeStart == "L":
            # print("A")
            uniqueEdges += 1
        elif v == "7" and lastEdgeStart == "F":
            # print("B")
            uniqueEdges += 2
        elif v == "J" and lastEdgeStart == "L":
            # print("C")
            uniqueEdges += 2
        elif v == "J" and lastEdgeStart == "F":
            # print("D")
            uniqueEdges += 1
        elif v == "|":
            # print("E")
            uniqueEdges += 1

    return uniqueEdges


def uniqueEdgesTop(pipeMap: list, point: tuple):
    uniqueEdges = 0

    lastEdgeStart = None

    for y in range(point[1], -1, -1):
        v = pipeMap[y][point[0]]

        if v in ["L", "J"]:
            lastEdgeStart = v

        if v == "7" and lastEdgeStart == "L":
            # print("A")
            uniqueEdges += 1
        elif v == "7" and lastEdgeStart == "J":
            # print("B")
            uniqueEdges += 2
        elif v == "F" and lastEdgeStart == "L":
            # print("C")
            uniqueEdges += 2
        elif v == "F" and lastEdgeStart == "J":
            # print("D")
            uniqueEdges += 1
        elif v == "-":
            # print("E")
            uniqueEdges += 1

    return uniqueEdges


def uniqueEdgesBottom(pipeMap: list, point: tuple):
    uniqueEdges = 0

    lastEdgeStart = None

    for y in range(point[1], len(pipeMap), 1):
        v = pipeMap[y][point[0]]

        if v in ["7", "F"]:
            lastEdgeStart = v

        if v == "L" and lastEdgeStart == "7":
            # print("A")
            uniqueEdges += 1
        elif v == "L" and lastEdgeStart == "F":
            # print("B")
            uniqueEdges += 2
        elif v == "J" and lastEdgeStart == "7":
            # print("C")
            uniqueEdges += 2
        elif v == "J" and lastEdgeStart == "F":
            # print("D")
            uniqueEdges += 1
        elif v == "-":
            # print("E")
            uniqueEdges += 1

    return uniqueEdges


def isPointOnInsideOfPipe(pipeMap: list, point: tuple):
    left = uniqueEdgesLeft(pipeMap, point)
    right = uniqueEdgesRight(pipeMap, point)
    top = uniqueEdgesTop(pipeMap, point)
    bottom = uniqueEdgesBottom(pipeMap, point)

    # print(left)
    # print(right)
    # print(top)
    # print(bottom)

    if left == 0 or right == 0 or top == 0 or bottom == 0:
        return False

    m = min([top, bottom, left, right])

    return not m % 2 == 0


def pt1():
    loop = findLoop(data)

    ans = int(len(loop) / 2)

    print(ans)
    return ans


def pt2():
    loop = findLoop(data)

    # printLoop(loop, data)
    # print()

    ans = 0

    z = replaceSWith(data)
    for x in range(len(data)):
        data[x] = data[x].replace("S", z)

    removeBadPipes(data, loop)

    # printLoop(loop, data)

    for y in range(len(data)):
        for x in range(len(data[y])):
            tup = (x, y)
            if tup not in loop:
                # print(f"{tup} | {isInLoop}")

                isInLoop = isPointOnInsideOfPipe(data, tup)

                if isInLoop:
                    # print(f"{tup} | {isInLoop}")
                    ans += 1

    print(ans)


print("Part 1 Answer:")
start_time = time.time()
pt1()
print(f"It took {time.time() - start_time}s to get answer")
start_time = time.time()
print("Part 2 Answer:")
pt2()
print(f"It took {time.time() - start_time}s to get answer")
