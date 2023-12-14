import os
import time

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def calculateColumnScoreEasy(col: list):
    colScore = 0

    t = "".join(col)

    # print(t)

    startPoints = list()

    for x in range(len(t) - 1):
        x1 = t[x]
        x2 = t[x + 1]

        if x == 0 and x1 != "#":
            startPoints.append(x)

        if x1 == "#" and x2 != "#":
            startPoints.append(x + 1)

    for z in range(len(startPoints)):
        start = startPoints[z]
        if z != len(startPoints) - 1:
            end = startPoints[z + 1]
        else:
            end = len(t)

        ss = t[start:end]

        # print(ss)
        numMovableRocks = ss.count("O")
        valueOfStartRow = len(col) - start

        for z in range(numMovableRocks):
            colScore += valueOfStartRow - z

    return colScore


def printPlatform(platform: list):
    for x in platform:
        print(x)
    print()


def getRotatedPlatformClockwise(platform: list):
    newPlatform = list()

    for x in range(len(platform[0])):
        newRow = list()
        for y in range(len(platform) - 1, -1, -1):
            newRow.append(platform[y][x])
        newPlatform.append("".join(newRow))

    return newPlatform


def shiftRocksUp(platform: list):
    newPlatform = list()

    for x in platform:
        newPlatform.append(list(x))

    for y in range(len(newPlatform)):
        for x in range(len(newPlatform[y])):
            currentSpot = newPlatform[y][x]

            if currentSpot == "O":
                check = y - 1
                while check >= 0:
                    if newPlatform[check][x] != ".":
                        break
                    check -= 1

                newPlatform[y][x] = "."
                newPlatform[check + 1][x] = "O"

    return newPlatform


def performCycle(platform: list):
    a = shiftRocksUp(platform)
    a = getRotatedPlatformClockwise(a)
    a = shiftRocksUp(a)
    a = getRotatedPlatformClockwise(a)
    a = shiftRocksUp(a)
    a = getRotatedPlatformClockwise(a)
    a = shiftRocksUp(a)
    a = getRotatedPlatformClockwise(a)

    return a


def hashToPlatform(hash: str, l: int):
    p = list()

    for x in range(int(len(hash) / l)):
        p.append(hash[x * l : (x * l) + l])

    return p


def calculateLoadOnNorthBeam(platform: list):
    ans = 0

    for y in range(len(platform)):
        # print(platform[y])
        for x in range(len(platform[y])):
            if platform[y][x] == "O":
                ans += len(platform) - y

    return ans


def toHash(state: list):
    return "".join(state)


def pt1():
    ans = 0

    for x in range(len(data[0])):
        currentCol = list()

        for y in range(len(data)):
            val = data[y][x]

            # print(val, end="")
            currentCol.append(val)

        colScore = calculateColumnScoreEasy(currentCol)
        # print(f"COL SCORE = {colScore}")
        ans += colScore

    print(ans)
    return ans


def pt2():
    factor = 1000000000
    runs = int(factor / 1000000)

    partitionSize = len(data[0])

    states = dict()

    currentState = toHash(data)

    for x in range(0, runs + 1):
        # if x % 100000 == 0:
        #     print(f"\r{round(((x / runs) * 100), 2)}%", end="")

        hash = toHash(currentState)

        if hash in states:
            # print(f"{x} | HIT")
            states[hash]["hits"] += 1
            nextState = states[hash]["next"]
        else:
            # print(f"{x} | MISS")
            nextState = toHash(
                performCycle(hashToPlatform(currentState, partitionSize))
            )
            states[hash] = {"next": nextState, "cycle": x, "hits": 0}

        currentState = nextState

    # print()

    uniqueStates = len(states.keys())

    repeatedStates = list()

    for x in states:
        if states[x]["hits"] > 0:
            repeatedStates.append(x)

    # for x in repeatedStates:
    #     state = hashToPlatform(x, partitionSize)
    #     stress = calculateLoadOnNorthBeam(state)
    #     print(f"{states[x]['cycle']} | {states[x]['hits']} | {stress} |")

    # print(f"{uniqueStates} unique states")
    # print(f"{len(repeatedStates)} repeated states")

    z = uniqueStates - len(repeatedStates)
    a = factor - z
    b = a % len(repeatedStates)
    c = z + b

    # print(z)
    # print(a)
    # print(b)
    # print(c)

    ans = 0

    for x in repeatedStates:
        if states[x]["cycle"] == c:
            state = hashToPlatform(x, partitionSize)
            stress = calculateLoadOnNorthBeam(state)
            ans = stress

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
