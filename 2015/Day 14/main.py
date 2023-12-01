import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input_test.txt"
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

        deers[name] = {
            "speed": speed,
            "stamina": stamina,
            "restPeriod": restPeriod,
            "cDistance": 0,
            "cResting": False,
            "cSpent": 0,
        }

    return deers


def pt1():
    deers = getStats(data)

    print(deers)

    secondsToCount = 1000

    for currentTime in range(secondsToCount):
        print("Iteration: ", currentTime + 1)
        for d in deers.keys():
            deer = deers[d]

            if deer["cResting"]:
                if deer["cSpent"] == deer["restPeriod"]:
                    deer["cResting"] = False
                    deer["cSpent"] = 0
            else:
                if deer["cSpent"] == deer["stamina"]:
                    deer["cResting"] = True
                    deer["cSpent"] = 0

                deer["cDistance"] = deer["cDistance"] + deer["speed"]

            deer["cSpent"] = deer["cSpent"] + 1

    print(deers)


def pt2():
    pass


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
