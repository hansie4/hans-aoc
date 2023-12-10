import os
import time

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input_test.txt"
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

    print(f"Starting at {currentPipe}")

    while True:
        visited.add(currentPipe)

        nextPipes = getNextPossiblePipes(pipeMap, currentPipe, visited)

        # print(nextPipes)

        if len(nextPipes) == 0:
            break

        currentPipe = nextPipes[0]

    return visited


def isPointOnInsideOfPipe(pipeMap: list, point: tuple):
    countToTheLeft = 0

    for x in range(point[0], -1, -1):
        if (
            pipeMap[point[1]][x] == "|"
            or pipeMap[point[1]][x] == "|"
            or pipeMap[point[1]][x] == "|"
        ):
            countToTheLeft += 1

    print("Left: ", countToTheLeft)

    countToTheRight = 0

    for x in range(point[0], len(pipeMap[point[0]]), 1):
        if pipeMap[point[1]][x] != ".":
            countToTheRight += 1

    print("Right: ", countToTheRight)


def printLoop(loop: set):
    for y in range(len(data)):
        for x in range(len(data[y])):
            if (x, y) in loop:
                char = data[y][x]
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
                print("╳", end="")
        print()


def pt1():
    loop = findLoop(data)

    ans = int(len(loop) / 2)

    print(ans)
    return ans


def pt2():
    loop = findLoop(data)

    printLoop(loop)

    isPointOnInsideOfPipe(data, (3, 2))


print("Part 1 Answer:")
start_time = time.time()
pt1()
print(f"It took {time.time() - start_time}s to get answer")
start_time = time.time()
print("Part 2 Answer:")
pt2()
print(f"It took {time.time() - start_time}s to get answer")
