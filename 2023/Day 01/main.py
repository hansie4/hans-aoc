import os
import re

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getCalibrationValue(s: str, valueDictionary: dict):
    locations = dict()

    for x in valueDictionary.keys():
        locations[x] = (None, None)

    # print(locations)

    for x in locations.keys():
        l = [m.start() for m in re.finditer("(?={})".format(x), s)]
        l.sort()
        # print(x + " | " + str(l))
        if l:
            locations[x] = (l[0], l[-1], valueDictionary[x])

    # print(locations)

    minIndex = len(s)
    maxIndex = -1
    minValue = None
    maxValue = None
    for x in locations.keys():
        if locations[x][0] != None and locations[x][0] < minIndex:
            minIndex = locations[x][0]
            minValue = locations[x][2]

        if locations[x][1] != None and locations[x][1] > maxIndex:
            maxIndex = locations[x][1]
            maxValue = locations[x][2]

    # print(minValue)
    # print(maxValue)
    # print(f"{s} | {(minValue * 10) + maxValue}")

    return (minValue * 10) + maxValue


def pt1():
    total = 0

    valueDict = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    for x in data:
        total += getCalibrationValue(x, valueDict)

    print(total)


def pt2():
    total = 0

    valueDict = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for x in data:
        total += getCalibrationValue(x, valueDict)

    print(total)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
