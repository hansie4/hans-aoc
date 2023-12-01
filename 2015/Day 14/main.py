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


def pt1():
    deers = getStats(data)

    # print(deers)

    simLength = 2503

    winner = ("", 0)

    for x in deers.keys():
        dis = simDeer(
            simLength, deers[x]["speed"], deers[x]["stamina"], deers[x]["restPeriod"]
        )

        if dis > winner[1]:
            winner = (x, dis)

    print(winner)


def pt2():
    pass


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
