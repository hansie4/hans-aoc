import os
import itertools

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getAllSubLists(l: list):
    everySubList = list()

    for a in range(len(l)):
        for b in range(a, len(l)):
            subList = l[a : b + 1]
            everySubList.append(subList)

    everySubList.remove(l)

    return everySubList


def pt1():
    total = 150

    containers = list(map(lambda x: int(x), data))
    containers.sort()

    # print(containers)

    ans = 0

    for x in range(len(containers)):
        combos = list(itertools.combinations(containers, x + 1))

        filteredList = list(filter(lambda z: sum(z) == total, combos))

        ans += len(filteredList)

    print(ans)


def pt2():
    total = 150

    containers = list(map(lambda x: int(x), data))
    containers.sort()

    # print(containers)

    ans = 0

    for x in range(len(containers)):
        combos = list(itertools.combinations(containers, x + 1))

        filteredList = list(filter(lambda z: sum(z) == total, combos))

        if len(filteredList) > 0:
            ans = len(filteredList)
            break

    print(ans)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
