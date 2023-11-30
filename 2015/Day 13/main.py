import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getHappinessLookup():
    lookup = dict()

    for x in data:
        t = x[:-1].split()

        p1 = t[0]
        p2 = t[10]
        hv = int(t[3]) if t[2] == "gain" else (-1 * int(t[3]))

        if p1 not in lookup.keys():
            lookup[p1] = dict()

        lookup[p1][p2] = hv

    return lookup


def pt1():
    lookup = getHappinessLookup()

    print(lookup)


def pt2():
    pass


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
