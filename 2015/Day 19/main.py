import os
import re

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getTransitions(info: list):
    transitions = list(map(lambda x: x.split(" => "), info[:-2]))

    tdict = dict()

    for x in transitions:
        if x[0] in tdict.keys():
            tdict[x[0]].append(x[1])
        else:
            tdict[x[0]] = []
            tdict[x[0]].append(x[1])

    # print(tdict)

    return tdict


def getCombos(transitions: dict, molecule: str):
    combos = set()

    for k in transitions.keys():
        locations = [m.start() for m in re.finditer("(?={})".format(k), molecule)]

        for x in transitions[k]:
            for y in locations:
                replaceFrom = k
                replaceTo = x

                firstHalf = molecule[0:y]
                secondHalf = molecule[y + len(replaceFrom) : len(molecule)]

                combos.add("".join([firstHalf, replaceTo, secondHalf]))

        # print(locations)

    return combos


def pt1():
    transitions = getTransitions(data)
    molecule = data[-1].strip()

    # print(transitions)
    # print(molecule)
    # print()

    combos = getCombos(transitions, molecule)
    print(len(combos))

    return len(combos)


def pt2():
    pass


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
