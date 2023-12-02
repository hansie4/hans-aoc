import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getStats(info):
    deers = dict()

    for x in info:
        t = x.split()
        name = t[0]
        speed = int(t[3])
        stamina = int(t[6])
        restPeriod = int(t[13])

        deers[name] = {"speed": speed, "stamina": stamina, "restPeriod": restPeriod}

    return deers


def simDeer(time: int, speed: int, stamina: int, restPeriod: int):
    # Old code no longer needed but used to make improved version
    isResting = False
    distance = 0
    restingFor = 0
    runningFor = 0
    for x in range(time):
        if isResting:
            restingFor += 1

            if restingFor == restPeriod:
                isResting = False
                restingFor = 0
        else:
            distance += speed
            runningFor += 1

            if runningFor == stamina:
                isResting = True
                runningFor = 0

    return distance


def simDeers(time: int, deers: dict):
    deerNames = list(deers.keys())
    isResting = [False] * len(deerNames)
    distances = [0] * len(deerNames)
    restingFor = [0] * len(deerNames)
    runningFor = [0] * len(deerNames)
    scores = [0] * len(deerNames)

    for x in range(time):
        for y in range(len(deerNames)):
            if isResting[y]:
                restingFor[y] = restingFor[y] + 1

                if restingFor[y] == deers[deerNames[y]]["restPeriod"]:
                    isResting[y] = False
                    restingFor[y] = 0
            else:
                distances[y] = distances[y] + deers[deerNames[y]]["speed"]
                runningFor[y] = runningFor[y] + 1

                if runningFor[y] == deers[deerNames[y]]["stamina"]:
                    isResting[y] = True
                    runningFor[y] = 0

        maxDist = max(distances)
        for y in range(len(distances)):
            if distances[y] == maxDist:
                scores[y] = scores[y] + 1

        # print(distances)
        # print(scores)

    return (max(distances), max(scores))


def printDict(d: dict):
    for x in d:
        print(x)
        for y in d[x]:
            print(y, ":", d[x][y])

        print()


def pt1():
    simLength = 2503

    deers = getStats(data)

    # printDict(deers)

    ans = simDeers(simLength, deers)[0]

    print(ans)


def pt2():
    simLength = 2503

    deers = getStats(data)

    # printDict(deers)

    ans = simDeers(simLength, deers)[1]

    print(ans)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
