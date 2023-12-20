import os
import time
from colorama import Fore, Style
from collections import deque

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def readInModules():
    modules = dict()

    for l in data:
        t = l.split(" -> ")

        if t[0] == "broadcaster":
            name = t[0]
            type = None
        else:
            name = t[0][1:]
            type = t[0][0]

        locations = t[1].replace(" ", "").split(",")

        for k in locations:
            if k not in modules.keys():
                modules[k] = {"type": None, "locations": []}

        modules[name] = {"type": type, "locations": locations}

    return modules


def getCunjunctionMap(modules: dict):
    conjunctionMap = dict()

    for x in modules.keys():
        if modules[x]["type"] == "&":
            conjunctionMap[x] = dict()

    for x in modules.keys():
        if modules[x]["type"] == "&":
            for y in modules:
                locs = modules[y]["locations"]

                if x in locs:
                    conjunctionMap[x][y] = 0

    return conjunctionMap


def countPulses(modules: dict, cunjunctionMap: dict, currentState: dict):
    queue = deque([("button", 0, "broadcaster")])

    lowPulseCount = 0
    highPulseCount = 0

    while len(queue) > 0:
        currentInstruction = queue.popleft()

        if currentInstruction[1] == 0:
            lowPulseCount += 1
        else:
            highPulseCount += 1

        # print(
        #     f"{currentInstruction[0]} {'-low' if currentInstruction[1] == 0 else '-high'}-> {currentInstruction[2]}"
        # )

        fro = currentInstruction[0]
        to = currentInstruction[2]

        if to == "broadcaster":
            for z in modules[to]["locations"]:
                queue.append((to, 0, z))
        elif to == "output":
            pass
        else:
            if modules[to]["type"] == "%":
                if currentInstruction[1] == 0:
                    currentState[to] = not currentState[to]

                    pulseLevel = 1 if currentState[to] else 0

                    for z in modules[to]["locations"]:
                        queue.append((to, pulseLevel, z))
            elif modules[to]["type"] == "&":
                # Update memory
                cunjunctionMap[to][fro] = currentInstruction[1]

                if len(cunjunctionMap[to].keys()) == sum(cunjunctionMap[to].values()):
                    for z in modules[to]["locations"]:
                        queue.append((to, 0, z))
                else:
                    for z in modules[to]["locations"]:
                        queue.append((to, 1, z))

            else:
                if currentInstruction[1] == 0:
                    print(currentInstruction)

    return lowPulseCount, highPulseCount


def pt1():
    modules = readInModules()

    conMap = getCunjunctionMap(modules)

    # for x in modules:
    #     print(f"{x} | {modules[x]}")

    currentState = dict()
    for x in modules:
        if modules[x]["type"] == "%":
            currentState[x] = False

    totalLow = 0
    totalHigh = 0

    for _ in range(1000):
        lp, hp = countPulses(modules, conMap, currentState)
        totalLow += lp
        totalHigh += hp

    # print(totalLow)
    # print(totalHigh)

    return totalHigh * totalLow


def pt2():
    pass


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
