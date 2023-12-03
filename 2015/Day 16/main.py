import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()

TICKER_TAPE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def importSues(info: list):
    sues = list()
    for x in info:
        currentSue = dict()

        t = x.replace(",", "")
        t = t.split(":", 1)
        id = t[0]
        t = t[1].replace(":", "").split()

        currentSue["id"] = id

        for z in range(0, len(t), 2):
            currentSue[t[z]] = int(t[z + 1])

        sues.append(currentSue)

    return sues


def filterSue(sue: dict):
    for x in TICKER_TAPE.keys():
        if x in sue.keys():
            if x in ["cats", "trees"]:
                if sue[x] < TICKER_TAPE[x]:
                    return False
            elif x in ["pomeranians", "goldfish"]:
                if sue[x] > TICKER_TAPE[x]:
                    return False
            else:
                if sue[x] != TICKER_TAPE[x]:
                    return False

    return True


def pt1():
    sues = importSues(data)

    # print(sues)

    filteredSues = sues.copy()

    for x in TICKER_TAPE.keys():
        filteredSues = list(
            filter(lambda z: x not in z.keys() or z[x] == TICKER_TAPE[x], filteredSues)
        )
        # print(filteredSues)

    ans = filteredSues.pop()["id"]
    print(ans)
    return ans


def pt2():
    sues = importSues(data)

    # print(sues)

    filteredSues = list(filter(filterSue, sues))

    ans = filteredSues.pop()["id"]
    print(ans)
    return ans


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
