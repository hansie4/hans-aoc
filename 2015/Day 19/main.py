import os
import re
import math

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input_test.txt"
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


# Got the answer from https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/ . This was a very hard one.
def pt2():
    molecule = data[-1].strip()

    l1 = 0
    l2 = 0
    l3 = 0

    for z in range(len(molecule)):
        x = molecule[z]
        k = x

        if z < len(molecule) - 1:
            k = "".join([molecule[z], molecule[z + 1]])

        if k == "Rn" or k == "Ar":
            l2 += 1
            l1 += 1
        elif x == "Y":
            l3 += 1
            l1 += 1
        elif x.isupper():
            l1 += 1

    # print(l1)
    # print(l2)
    # print(l3)

    ans = l1 - l2 - (2 * l3) - 1

    print(ans)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
