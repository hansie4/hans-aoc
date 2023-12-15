import os
import time

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().split(",")


def removeFromList(l: list, indexToRemove: int):
    return l[:indexToRemove] + l[indexToRemove + 1 :]


def replaceInList(l: list, indexToReplace: int, newValue):
    return l[:indexToReplace] + [newValue] + l[indexToReplace + 1 :]


def pt1Hash(s: str):
    hashValue = 0

    for c in s:
        charVal = ord(c)
        hashValue += charVal
        hashValue *= 17
        hashValue = hashValue % 256

    return hashValue


def printBoxes(boxes: list):
    for x in range(len(boxes)):
        if len(boxes[x]) > 0:
            print(f"Box {x}: {boxes[x]}")

    print()


def calculateFocusingPower(boxes: list):
    focusingPower = 0

    for x in range(len(boxes)):
        for y in range(len(boxes[x])):
            p = (x + 1) * (y + 1) * (boxes[x][y][1])
            focusingPower += p

    return focusingPower


def pt1():
    ans = 0

    for x in data:
        ans += pt1Hash(x)

    print(ans)
    return ans


def pt2():
    boxes = [[] for _ in range(256)]

    for x in data:
        EQUALS_OPERATION = "=" in x

        if EQUALS_OPERATION:
            t = x.split("=")
        else:
            t = x.split("-")

        label = t[0]

        box = pt1Hash(label)

        # print(f"{label} | {box} | {EQUALS_OPERATION}")

        indexWithLabel = next(
            (i for i, x in enumerate(boxes[box]) if x[0] == label), None
        )

        if EQUALS_OPERATION:
            focalLength = int(t[1])

            lensTuple = (label, focalLength)

            if indexWithLabel != None:
                boxes[box] = replaceInList(boxes[box], indexWithLabel, lensTuple)
            else:
                boxes[box].append(lensTuple)
        else:
            if indexWithLabel != None:
                boxes[box] = removeFromList(boxes[box], indexWithLabel)

        # print(f'After "{x}"')
        # printBoxes(boxes)

    ans = calculateFocusingPower(boxes)

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
