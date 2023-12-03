import os


script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()

MAX_TEASPOONS = 100

COOKIE_FIELDS = ["capacity", "durability", "flavor", "texture", "calories"]


def getCookieStats(info: list, withCalories: bool):
    cookieStats = dict()

    for x in info:
        t = x.replace(",", " ")
        t = t.replace(":", " ")
        t = t.split()
        # print(t)
        name = t[0]
        capacity = int(t[2])
        durability = int(t[4])
        flavor = int(t[6])
        texture = int(t[8])
        calories = int(t[10])

        cookieStats[name] = {
            COOKIE_FIELDS[0]: capacity,
            COOKIE_FIELDS[1]: durability,
            COOKIE_FIELDS[2]: flavor,
            COOKIE_FIELDS[3]: texture,
        }

        if withCalories:
            cookieStats[name][COOKIE_FIELDS[4]] = calories

    return cookieStats


def getScore(ingredientStats: dict, ingredientAmounts: dict):
    score = 1

    statLists = list()

    for x in ingredientAmounts.keys():
        amount = ingredientAmounts[x]

        stats = [0] * len(COOKIE_FIELDS[:-1])

        for y in range(len(stats)):
            stats[y] = ingredientStats[x][COOKIE_FIELDS[y]]

        stats = list(map(lambda z: z * amount, stats))

        statLists.append(stats)

    finalStatList = [0] * len(statLists[0])

    for y in range(len(finalStatList)):
        # print(y)
        acc = 0
        for x in range(len(statLists)):
            # print(statLists[x][y])
            acc += statLists[x][y]
        finalStatList[y] = acc

    for x in finalStatList:
        valueToUse = x

        if x < 0:
            valueToUse = 0

        score *= valueToUse

    # print(score)

    return score


def getCalorieTotal(ingredientStats: dict, ingredientAmounts: dict):
    ingredients = list(ingredientStats.keys())
    calorieAmounts = list(ingredientStats.keys())
    final = list(ingredientStats.keys())

    for x in range(len(ingredients)):
        calorieAmounts[x] = ingredientStats[ingredients[x]]["calories"]

    for x in range(len(ingredients)):
        final[x] = calorieAmounts[x] * ingredientAmounts[ingredients[x]]

    # print(calorieAmounts)
    # print(ingredientAmounts)
    # print(final)

    return sum(final)


def testAmount(ingredientList: list, ingredientStats: dict, values: list):
    testAmounts = dict()

    if sum(values) != MAX_TEASPOONS:
        print("INVALID VALUES")

    for x in range(len(ingredientList)):
        testAmounts[ingredientList[x]] = values[x]

    score = getScore(ingredientStats, testAmounts)

    # print(f"{score} | {testAmounts}")

    return score


def testAmountPt2(ingredientList: list, ingredientStats: dict, values: list):
    testAmounts = dict()

    if sum(values) != MAX_TEASPOONS:
        print("INVALID VALUES")

    for x in range(len(ingredientList)):
        testAmounts[ingredientList[x]] = values[x]

    if getCalorieTotal(ingredientStats, testAmounts) != 500:
        return 0

    score = getScore(ingredientStats, testAmounts)

    # print(f"{score} | {testAmounts}")

    return score


def generateTestValues(theSum: int):
    testValues = []

    for a in range(theSum):
        for b in range(theSum):
            if sum([a, b]) <= theSum:
                for c in range(theSum):
                    if sum([a, b, c]) <= theSum:
                        for d in range(theSum):
                            if sum([a, b, c, d]) == theSum:
                                testValues.append([a, b, c, d])

    return testValues


def pt1():
    ingredientStats = getCookieStats(data, False)

    ingredientList = list(ingredientStats.keys())

    testAmounts = generateTestValues(MAX_TEASPOONS)

    topScore = 0

    for x in testAmounts:
        s = testAmount(ingredientList, ingredientStats, x)
        if s > topScore:
            topScore = s

    print(topScore)


def pt2():
    ingredientStats = getCookieStats(data, True)

    ingredientList = list(ingredientStats.keys())

    testAmounts = generateTestValues(MAX_TEASPOONS)

    topScore = 0

    for x in testAmounts:
        s = testAmountPt2(ingredientList, ingredientStats, x)
        if s > topScore:
            topScore = s

    print(topScore)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
