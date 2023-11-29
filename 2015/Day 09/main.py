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


# Needs to take a list of paths a current route and output a list of the routes that can be taken from the current route
def shortestPath(nodes: set, paths: dict, route: list):
    # print("Looking for path from ", route)
    # Base case all have been met or current node has none it can travel to

    if len(route) == len(nodes):
        # print("Route Found: ", route)

        d = 0

        for x in range(len(route) - 1):
            f = route[x]
            t = route[x + 1]

            d += paths[f][t]

        return route, d

    cityFrom = route[:1].pop()

    if len(paths[cityFrom].keys()) == 0:
        return None

    routeList = list()

    for x in paths[cityFrom].keys():
        if x not in route:
            newRoute = route.copy()
            newRoute.append(x)
            # print("New route: ", newRoute)
            newPath = shortestPath(nodes, paths, newRoute)

            if newPath:
                routeList.append(newPath)

    return routeList


def pt1():
    r = readInRoutes()

    paths = dict()

    nodes = set()

    for x in r:
        nodes.add(x[0])
        nodes.add(x[1])

    for x in nodes:
        paths[x] = {}

    for x in r:
        paths[x[0]][x[1]] = int(x[2])
        paths[x[1]][x[0]] = int(x[2])

    # print(nodes)
    # print(paths)

    routes = list()

    for x in nodes:
        p = shortestPath(nodes, paths, [x])
        for z in p:
            routes.append(z)

    # routes.sort(key=lambda x: x[0][1])

    flattened = list()
    # print("---------------------")
    for x in routes:
        for y in x:
            for z in y:
                for aa in z:
                    for bb in aa:
                        for zz in bb:
                            flattened.append(zz[0])

    flattened.sort(key=lambda z: z[1])
    flattened.reverse()

    # for x in flattened:
    #     print(x)

    ans1 = flattened.pop()[1]
    flattened.reverse()
    ans2 = flattened.pop()[1]

    return ans1, ans2


print("Part 1 Answer:")
ans = pt1()
print(ans[0])
print("Part 2 Answer:")
print(ans[1])
