import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getHappinessLookup(info):
    lookup = dict()

    for x in info:
        t = x[:-1].split()

        p1 = t[0]
        p2 = t[10]
        hv = int(t[3]) if t[2] == "gain" else (-1 * int(t[3]))

        if p1 not in lookup.keys():
            lookup[p1] = dict()

        lookup[p1][p2] = hv

    return lookup


def getAllNeighborCombos(people: set, currentSeating: list, combos: list):
    if len(currentSeating) == len(people):
        combos.append(currentSeating)

    for x in people:
        newSeating = currentSeating.copy()
        if x not in newSeating:
            newSeating.append(x)

            getAllNeighborCombos(people, newSeating, combos)


def calculateHappiness(lookup: dict, seating: list):
    total = 0
    for x in range(len(seating)):
        p1 = seating[x]
        if x == len(seating) - 1:
            p2 = seating[0]
        else:
            p2 = seating[x + 1]

        happiness = lookup[p1][p2] + lookup[p2][p1]

        total += happiness

    return total


def pt1():
    lookup = getHappinessLookup(data)

    # print(lookup)

    combos = list()

    getAllNeighborCombos(lookup.keys(), [], combos)

    for x in combos:
        x.append(calculateHappiness(lookup, x))

    combos.sort(key=lambda y: y[len(lookup.keys())])

    print(combos[-1])


def pt2():
    lookup = getHappinessLookup(data)

    peopleOtherThanMe = set()

    for x in lookup.keys():
        lookup[x]["Hans"] = 0
        peopleOtherThanMe.add(x)

    lookup["Hans"] = {}
    for x in peopleOtherThanMe:
        lookup["Hans"][x] = 0

    # print(lookup)

    combos = list()

    getAllNeighborCombos(lookup.keys(), [], combos)

    for x in combos:
        x.append(calculateHappiness(lookup, x))

    combos.sort(key=lambda y: y[len(lookup.keys())])

    print(combos[-1])


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
