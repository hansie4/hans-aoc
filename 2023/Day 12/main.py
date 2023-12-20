import os
import time
import itertools
import re
from cachetools import cached, TTLCache

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


globalCache = dict()


def replaceIndex(originalString: str, index: int, newValue: str):
    return originalString[:index] + newValue + originalString[index + 1 :]


def insertIndex(originalString: str, index: int, newValue: str):
    return originalString[:index] + newValue + originalString[index:]


def getSpringLocations(springs: str):
    goodSpringLocs = list()
    badSpringLocs = list()

    for x in range(len(springs)):
        s = springs[x]

        if s == "#":
            goodSpringLocs.append(x)
        elif s == "?":
            badSpringLocs.append(x)

    return goodSpringLocs, badSpringLocs


def mapInput(info: list):
    mappedData = list()

    for x in info:
        t = x.split()
        z = t[1].split(",")
        z = list(map(lambda i: int(i), z))

        mappedData.append((t[0], z))

    return mappedData


def splitStringUp(inputStringNotReady: str):
    indexesToInsertAt = list()

    inputString = inputStringNotReady.replace(".", " ")

    for x in range(len(inputString) - 1):
        v1 = inputString[x]
        v2 = inputString[x + 1]

        if (v1 == "?" and v2 == "#") or (v1 == "#" and v2 == "?"):
            indexesToInsertAt.append(x + 1)

    indexesToInsertAt.sort()

    newString = inputString

    for x in indexesToInsertAt[::-1]:
        newString = insertIndex(newString, x, " ")

    return newString.split()


def isStringValid(inputString: str, springs: list):
    s = inputString.replace(".", " ")
    s = s.replace("?", " ")
    s = s.split()

    if len(s) != len(springs):
        return False

    for x in range(len(springs)):
        if len(s[x]) != springs[x]:
            return False

    return True


def getPossibilities(inputString: str, springs: list):
    # print(inputString)

    goodSpringLocs, badSpringLocs = getSpringLocations(inputString)

    spotsToFillIn = sum(springs) - len(goodSpringLocs)

    # print(spotsToFillIn)
    # print(badSpringLocs)

    a = list(itertools.combinations(badSpringLocs, spotsToFillIn))

    numPoss = 0

    for x in a:
        testString = inputString

        for z in x[::-1]:
            testString = replaceIndex(testString, z, "#")

        # print(testString)

        k = isStringValid(testString, springs)

        if k:
            # print(testString)
            numPoss += 1

    return numPoss


def transformInput(factor: int, originalInput: list):
    newInput = list()

    for x in originalInput:
        n1 = "?".join([x[0]] * factor)
        n2 = x[1] * factor

        newInput.append((n1, n2))

    return newInput


def countAllPossibleValidWays(springMap: str, springGroups: list):
    if springMap == "":
        return 1 if len(springGroups) == 0 else 0
    elif len(springGroups) == 0:
        return 0 if "#" in springMap else 1
    else:
        if (springMap, tuple(springGroups)) in globalCache:
            return globalCache[(springMap, tuple(springGroups))]

        count = 0

        firstChar = springMap[0]

        if firstChar == "." or firstChar == "?":
            count += countAllPossibleValidWays(springMap[1:], springGroups)

        if firstChar == "#" or firstChar == "?":
            restOfSpringsCanFit = springGroups[0] <= len(springMap)
            nextGroupOfSpringSplitUp = "." in springMap[: springGroups[0]]

            if (
                restOfSpringsCanFit
                and not nextGroupOfSpringSplitUp
                and (
                    springGroups[0] == len(springMap)
                    or springMap[springGroups[0]] != "#"
                )
            ):
                count += countAllPossibleValidWays(
                    springMap[springGroups[0] + 1 :], springGroups[1:]
                )

        globalCache[(springMap, tuple(springGroups))] = count

        return count


def pt1():
    mappedInput = mapInput(data)

    ans = 0

    for x in mappedInput:
        p = getPossibilities(x[0], x[1])
        ans += p

    print(ans)
    return ans


def pt2():
    mappedInput = transformInput(5, mapInput(data))

    ans = 0

    for x in mappedInput:
        # print(x)
        c = countAllPossibleValidWays(x[0], x[1])
        ans += c

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
