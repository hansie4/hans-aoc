import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def readInRoutes():
    a = list()
    for x in data:
        t = x.split(" ")
        a.append((t[0], t[2], t[4]))
    return a


def shortestPath(paths: dict, node: str, visited: list, currentCost: int):
    print("Looking for path from ", node)
    # Base case all have been met or current node has none it can travel to
    lastNode = len(paths.keys()) > (len(visited) - 1)
    cantTravel = paths[node] == None
    if not cantTravel:
        for x in paths[node]:
            if x not in visited:
                cantTravel = False

    if lastNode or cantTravel:
        return currentCost

    return cost


def pt1():
    r = readInRoutes()

    # print(r)

    paths = dict()

    for x in r:
        if x[0] in paths:
            paths[x[0]][x[1]] = x[2]
        else:
            paths[x[0]] = {}
            paths[x[0]][x[1]] = int(x[2])

    for x in r:
        if x[1] not in paths:
            paths[x[1]] = None

    print(paths)

    print(shortestPath(paths, [], "London"))


def pt2():
    pass


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
