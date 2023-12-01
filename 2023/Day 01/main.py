import os
import re

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def replaceValues(k: str, reversed: bool):
    strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    x = k

    if reversed:
        x = k[::-1]
        for z in range(len(strings)):
            strings[z] = strings[z][::-1]

    # print(strings)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    indexes = [1000000] * len(strings)

    for s in range(len(strings)):
        try:
            indexes[s] = x.index(strings[s])
        except:
            indexes[s] = 1000000

    # print(indexes)

    firstIndex = indexes.index(min(indexes))

    newString = x.replace(strings[firstIndex], str(nums[firstIndex]), 1)

    if reversed:
        return newString[::-1]
    else:
        return newString


def pt1():
    values = list()
    for x in data:
        # print("Checking ", x)

        v1 = None
        v2 = None
        p1 = 0
        p2 = len(x) - 1

        for y in range(len(x)):
            if x[p1].isdigit():
                v1 = int(x[p1])

            if x[p2].isdigit():
                v2 = int(x[p2])

            if v1 == None:
                p1 += 1
            if v2 == None:
                p2 -= 1

            if v1 and v2:
                break

        values.append((v1 * 10) + v2)

    print(sum(values))


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


def getCalibrationValue(s: str):
    locations = dict()

    thingsToLookFor = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for x in thingsToLookFor:
        locations[x] = (None, None)

    # print(locations)

    for x in locations.keys():
        l = [m.start() for m in re.finditer("(?={})".format(x), s)]
        l.sort()
        # print(x + " | " + str(l))
        if l:
            locations[x] = (l[0], l[-1], valueDict[x])

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


def pt2():
    total = 0

    for x in data:
        total += getCalibrationValue(x)

    print(total)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
