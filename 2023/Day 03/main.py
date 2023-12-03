import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read()

SYMBOLS = ["*", "%", "#", "+", "%", "/", "@", "=", "$", "&", "-"]


def getNumbers(info: list):
    t = info.replace(".", " ")

    for x in SYMBOLS:
        t = t.replace(x, " ")

    numbers = t.split()
    numbers = list(map(lambda x: int(x), numbers))

    return numbers


def isNearSymbol(info: list, digitX: int, digitY: int):
    cordsToCheck = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]
    lengthOfRow = len(info[0])

    if digitX == 0:
        cordsToCheck.remove((-1, -1))
        cordsToCheck.remove((-1, 0))
        cordsToCheck.remove((-1, 1))

    if digitX == lengthOfRow - 1:
        cordsToCheck.remove((1, -1))
        cordsToCheck.remove((1, 0))
        cordsToCheck.remove((1, 1))

    if digitY == 0:
        if (-1, -1) in cordsToCheck:
            cordsToCheck.remove((-1, -1))
        if (0, -1) in cordsToCheck:
            cordsToCheck.remove((0, -1))
        if (1, -1) in cordsToCheck:
            cordsToCheck.remove((1, -1))

    if digitY == len(info) - 1:
        if (-1, 1) in cordsToCheck:
            cordsToCheck.remove((-1, 1))
        if (0, 1) in cordsToCheck:
            cordsToCheck.remove((0, 1))
        if (1, 1) in cordsToCheck:
            cordsToCheck.remove((1, 1))

    # print(cordsToCheck)

    for x in cordsToCheck:
        if info[digitY + x[1]][digitX + x[0]] in SYMBOLS:
            return True

    return False


def pt1():
    numbers = getNumbers(data)
    counted = [False] * len(numbers)

    # print(numbers)
    # print(counted)

    rows = data.splitlines()

    currentNumber = 0
    lastValue = "."

    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if rows[y][x].isdigit():
                test = isNearSymbol(rows, x, y)
                # print(rows[y][x] + " | " + str(test))
                if test:
                    counted[currentNumber] = True
            else:
                if lastValue.isdigit():
                    currentNumber += 1

            lastValue = rows[y][x]

    # print(counted)

    ans = 0

    for x in range(len(numbers)):
        if counted[x]:
            ans += numbers[x]

    print(ans)
    return ans


def pt2():
    pass


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
