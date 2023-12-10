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
    print(cp)

    if cp == "S":
        pass
    elif cp == "L":
        pass
    elif cp == "F":
        pass
    elif cp == "|":
        pass
    elif cp == "-":
        # Left pipe
        if currentPipe[0] != 0:
            nextPipeCords = (currentPipe[0] - 1, currentPipe[1])
            nextPipeType = pipeMap[nextPipeCords[1]][nextPipeCords[0]]
            if doPipesConnect(cp, pipeMap[currentPipe[1]][currentPipe[0] - 1]):
                nextPipes.append((currentPipe[0] - 1, currentPipe[1]))

    return nextPipes


def findLoop(pipeMap: list):
    visited = set()

    start = findStart(pipeMap)

    getNextPossiblePipe(pipeMap, start, visited)


def pt1():
    loop = findLoop(data)


def pt2():
    pass


print("Part 1 Answer:")
start_time = time.time()
pt1()
print(f"It took {time.time() - start_time}s to get answer")
start_time = time.time()
print("Part 2 Answer:")
pt2()
print(f"It took {time.time() - start_time}s to get answer")
