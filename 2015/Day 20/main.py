import os
import time
import math
import sys

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read()


def getPresentsForHouse(houseNumber: int):
    # lim = int(math.ceil(math.sqrt(houseNumber)))
    lim = int(math.ceil(houseNumber / 2))

    factors = [1]

    if houseNumber != 1:
        factors.append(houseNumber)

    for x in range(2, lim + 1):
        if houseNumber % x == 0:
            factors.append(x)

    # print(factors)

    return sum(factors) * 10


def getPresentsForHouse2(houseNumber: int):
    # lim = int(math.ceil(math.sqrt(houseNumber)))
    lim = int(math.ceil(houseNumber / 2))

    factors = []

    if houseNumber != 1:
        factors.append(houseNumber)

    for x in range(lim, 0, -1):
        if houseNumber % x == 0:
            factors.append(x)

        if len(factors) == 50:
            break

    # print(factors)
    # print(len(factors))

    return sum(factors) * 11


def pt1():
    gameInput = int(data)

    ans = sys.maxsize

    topRange = int(gameInput / 36)
    bottomRange = int(gameInput / 50)

    # print(getPresentsForHouse(806399))

    for x in range(bottomRange, topRange):
        presents = getPresentsForHouse(x)

        # print((x / gameInput) * 100)
        sys.stdout.write(f"{(((x - bottomRange) / (topRange - bottomRange)) * 100)}\r")
        sys.stdout.flush()

        if x % 1000 == 0:
            print(x)

        if presents >= gameInput:
            print(f"{presents} at house {x}")
            ans = x
            break

    print(ans)


def pt2():
    gameInput = int(data)

    ans = sys.maxsize

    topRange = 665280
    bottomRange = 30000

    for x in range(bottomRange, topRange):
        # presents1 = getPresentsForHouse(x)
        # presents2 = getPresentsForHouse2(x)

        # print(
        #     f"House {x} got {presents1} presents.\t|\t\tHouse {x} got {presents2} presents."
        # )

        presents = getPresentsForHouse2(x)

        # print((x / gameInput) * 100)
        sys.stdout.write(f"{(((x - bottomRange) / (topRange - bottomRange)) * 100)}\r")
        sys.stdout.flush()

        if x % 1000 == 0:
            print(x)

        if presents >= gameInput:
            print(f"{presents} at house {x}")
            ans = x
            break

    print(ans)


print("Part 1 Answer:")
start_time = time.time()
# pt1()
print(f"It took {time.time() - start_time}s to get answer")
start_time = time.time()
print("Part 2 Answer:")
pt2()
print(f"It took {time.time() - start_time}s to get answer")
