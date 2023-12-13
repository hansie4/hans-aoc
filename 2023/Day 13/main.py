import os
import time

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getInputs(info: list()):
    inputs = list()

    lastSplitAt = -1

    for x in range(len(info)):
        line = info[x]

        if len(line) == 0:
            inputs.append(info[lastSplitAt + 1 : x])
            lastSplitAt = x

    inputs.append(info[lastSplitAt + 1 :])

    return inputs


def findVerticalLineOfSym(m: list):
    for xI in range(len(m[0]) - 1):
        oL = xI + 1
        oR = len(m[0]) - (xI + 1)
        maxXOffset = min(oL, oR)
        # print()
        allMatch = True

        for yI in range(len(m)):
            for offset in range(maxXOffset):
                left = m[yI][xI - offset]
                right = m[yI][(xI + 1) + offset]

                # print(f"y={yI} | {left} <-> {right}")

                if left != right:
                    allMatch = False
                    # print("HERE")
                    break

        if allMatch and yI == len(m) - 1:
            return (xI, xI + 1)

    return None


def findVerticalLineOfSym2(m: list):
    locationOfVerticalLineOfSym = None
    locationOfPossibleNewLineOfSym = None

    for xI in range(len(m[0]) - 1):
        oL = xI + 1
        oR = len(m[0]) - (xI + 1)
        maxXOffset = min(oL, oR)
        # print()
        allMatch = True

        smudges = 0

        for yI in range(len(m)):
            for offset in range(maxXOffset):
                left = m[yI][xI - offset]
                right = m[yI][(xI + 1) + offset]

                if left != right:
                    allMatch = False
                    smudges += 1

        if allMatch and yI == len(m) - 1:
            locationOfVerticalLineOfSym = (xI, xI + 1)
        elif smudges == 1 and yI == len(m) - 1:
            locationOfPossibleNewLineOfSym = (xI, xI + 1)

    return (
        locationOfVerticalLineOfSym,
        locationOfPossibleNewLineOfSym,
    )


def findHorizontalLineOfSym(m: list):
    for yI in range(len(m) - 1):
        oU = yI + 1
        oD = len(m) - (yI + 1)
        maxYOffset = min(oU, oD)
        # print(maxYOffset)
        allMatch = True

        for xI in range(len(m[yI])):
            for offset in range(maxYOffset):
                top = m[yI - offset][xI]
                bottom = m[(yI + 1) + offset][xI]

                # print(f"x={xI} | {top} <-> {bottom}")

                if top != bottom:
                    allMatch = False
                    break

            if not allMatch:
                break

        if allMatch and xI == len(m[yI]) - 1:
            return (yI, yI + 1)

    return None


def findHorizontalLineOfSym2(m: list):
    locationOfHorizontalLineOfSym = None
    locationOfPossibleNewLineOfSym = None

    for yI in range(len(m) - 1):
        oU = yI + 1
        oD = len(m) - (yI + 1)
        maxYOffset = min(oU, oD)
        # print(maxYOffset)
        allMatch = True

        smudges = 0

        for xI in range(len(m[yI])):
            for offset in range(maxYOffset):
                top = m[yI - offset][xI]
                bottom = m[(yI + 1) + offset][xI]

                if top != bottom:
                    allMatch = False
                    smudges += 1

        if allMatch and xI == len(m[yI]) - 1:
            locationOfHorizontalLineOfSym = (yI, yI + 1)
        elif smudges == 1 and xI == len(m[yI]) - 1:
            locationOfPossibleNewLineOfSym = (yI, yI + 1)

    return (
        locationOfHorizontalLineOfSym,
        locationOfPossibleNewLineOfSym,
    )


def pt1():
    inputs = getInputs(data)

    ans = 0

    for x in inputs:
        v = findVerticalLineOfSym(x)

        if v:
            ans += v[0] + 1
        else:
            h = findHorizontalLineOfSym(x)

            ans += 100 * (h[0] + 1)

    print(ans)
    return ans


def pt2():
    inputs = getInputs(data)

    ans = 0

    for x in inputs:
        v = findVerticalLineOfSym2(x)
        h = findHorizontalLineOfSym2(x)

        if v[1] != None:
            ans += v[1][0] + 1
        elif h[1] != None:
            ans += 100 * (h[1][0] + 1)
        else:
            print("-------------")
            print(x)

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
