import os
import time
from colorama import Fore, Style

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def isInBounds(node: tuple, maxX: int, maxY: int):
    x = node[0]
    y = node[1]

    if x < 0 or y < 0 or x > maxX or y > maxY:
        return False

    return True


def getAllPossibleStarts(maxX: int, maxY: int):
    starts = set()

    for x in range(maxX + 1):
        s1 = (x, 0, "D")
        s2 = (x, maxY, "U")
        starts.add(s1)
        starts.add(s2)

    for y in range(maxY + 1):
        s3 = (0, y, "R")
        s4 = (maxX, y, "L")
        starts.add(s3)
        starts.add(s4)

    return starts


def getEnergizedSquares(start: tuple):
    currentNodes = set()
    currentNodes.add(start)

    energized = set()
    seen = set()

    seen.add((start[0], start[1]))
    energized.add((start[0], start[1]))

    while True:
        cn = currentNodes.copy()

        if len(cn) == 0:
            # print("DONE")
            break

        for n in cn:
            seen.add(n)
            currentDir = n[2]
            if currentDir == "U":
                nextNode = [n[0], n[1] - 1, n[2]]
            elif currentDir == "D":
                nextNode = [n[0], n[1] + 1, n[2]]
            elif currentDir == "L":
                nextNode = [n[0] - 1, n[1], n[2]]
            else:
                nextNode = [n[0] + 1, n[1], n[2]]

            if isInBounds(nextNode, len(data[0]) - 1, len(data) - 1):
                nextLocValue = data[nextNode[1]][nextNode[0]]

                nextDir = None
                nextDirs = None

                if nextLocValue == "\\":
                    if currentDir == "U":
                        nextDir = "L"
                    elif currentDir == "D":
                        nextDir = "R"
                    elif currentDir == "L":
                        nextDir = "U"
                    elif currentDir == "R":
                        nextDir = "D"
                    else:
                        print("THIS SHOULD NEVER HAPPEN 1")
                elif nextLocValue == "/":
                    if currentDir == "U":
                        nextDir = "R"
                    elif currentDir == "D":
                        nextDir = "L"
                    elif currentDir == "L":
                        nextDir = "D"
                    elif currentDir == "R":
                        nextDir = "U"
                    else:
                        print("THIS SHOULD NEVER HAPPEN 2")
                elif nextLocValue == "-" and currentDir in ["U", "D"]:
                    nextDirs = ["L", "R"]
                elif nextLocValue == "|" and currentDir in ["L", "R"]:
                    nextDirs = ["U", "D"]
                else:
                    nextDir = currentDir

                nextNodes = []

                if nextDir != None:
                    nextNode[2] = nextDir
                elif nextDirs != None:
                    for d in nextDirs:
                        nextNodes.append((nextNode[0], nextNode[1], d))
                else:
                    print("THIS SHOULD NEVER HAPPEN 3")

                # currentNodes.remove(n)

                if len(nextNodes) > 0:
                    for z in nextNodes:
                        t = tuple(z)
                        if t not in seen:
                            currentNodes.add(t)
                            energized.add((t[0], t[1]))
                else:
                    t = tuple(nextNode)
                    if t not in seen:
                        currentNodes.add(t)
                        energized.add((t[0], t[1]))

            currentNodes.remove(n)

        # energizedSpots = list(map(lambda x: (x[0], x[1]), list(energized)))
        # os.system("cls" if os.name == "nt" else "clear")
        # for y in range(len(data)):
        #     for x in range(len(data[y])):
        #         if (x, y) in energizedSpots:
        #             print("#", end="")
        #         else:
        #             print(".", end="")
        #     print()

        # input()

    ans = len(energized)
    return ans


def pt1():
    start = (0, 0, "R")

    ans = getEnergizedSquares(start)

    return ans


def pt2():
    starts = getAllPossibleStarts(len(data[0]) - 1, len(data) - 1)

    ans = 0

    for s in starts:
        t = getEnergizedSquares(s)

        if t > ans:
            ans = t

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
