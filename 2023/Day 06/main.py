import os
import time

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def readInData(info: dict):
    t = list(map(lambda x: int(x), info[0].replace("Time:", "").split()))
    d = list(map(lambda x: int(x), info[1].replace("Distance:", "").split()))

    return t, d


def race(holdTime, raceTime):
    return holdTime * raceTime


def pt1():
    t, d = readInData(data)

    wins = [0] * len(t)

    for x in range(len(t)):
        # print(f"RUN {x + 1}")
        time = t[x]
        minDist = d[x]

        for y in range(time + 1):
            raceDist = race(y, time - y)

            if raceDist > minDist:
                wins[x] = wins[x] + 1
            # print(race(y, time - y))

    # print(wins)
    ans = 1

    for x in wins:
        ans *= x

    print(ans)
    return ans


def pt2():
    newT = int("".join(data[0].split(":")[1].split()))
    newD = int("".join(data[1].split(":")[1].split()))

    ans = 0

    for y in range(newT + 1):
        raceDist = race(y, newT - y)

        if raceDist > newD:
            ans += 1

    print(ans)
    return ans


def pt3():
    newT = int("".join(data[0].split(":")[1].split()))
    newD = int("".join(data[1].split(":")[1].split()))

    bottom = None
    top = None

    ans = 0

    for y in range(newT + 1):
        raceDist = race(y, newT - y)

        if raceDist > newD:
            bottom = y
            break

    for y in range(newT + 1, -1, -1):
        raceDist = race(y, newT - y)

        if raceDist > newD:
            top = y
            break

    # print(bottom)
    # print(top)

    ans = top - bottom + 1

    print(ans)


print("Part 1 Answer:")
start_time = time.time()
pt1()
print(f"It took {time.time() - start_time}s to get answer")
start_time = time.time()
print("Part 2 Answer:")
pt2()
print(f"It took {time.time() - start_time}s to get answer")

start_time = time.time()
print("Part 2 Optimized Answer:")
pt3()
print(f"It took {time.time() - start_time}s to get answer")
