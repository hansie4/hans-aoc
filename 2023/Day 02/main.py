import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getValidGames(maxes: dict, info: list):
    validGames = [True] * len(info)

    for y in range(len(info)):
        x = info[y]
        t = x.split(":")[1].replace(",", "").replace(";", "").split()
        # print(t)

        for z in range(0, len(t), 2):
            num = int(t[z])
            color = t[z + 1]

            if maxes[color] < num:
                validGames[y] = False

    return validGames


def getPower(game: str):
    maxes = {"red": -1, "blue": -1, "green": -1}

    t = game.split(":")[1].split(";")

    # print(game)

    for g in t:
        t2 = g.replace(",", "").split()
        # print(t2)

        for z in range(0, len(t2), 2):
            num = int(t2[z])
            color = t2[z + 1]

            if maxes[color] < num:
                maxes[color] = num

    return maxes["red"] * maxes["green"] * maxes["blue"]


def pt1():
    maxes = {"red": 12, "blue": 14, "green": 13}

    validGames = getValidGames(maxes, data)

    # print(validGames)

    ans = 0

    for x in range(len(validGames)):
        if validGames[x]:
            ans += x + 1

    print(ans)


def pt2():
    total = 0

    for x in data:
        total += getPower(x)

    print(total)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
