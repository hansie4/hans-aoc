import os
import time
from colorama import Fore, Style

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()

ruleSet = []


def getInput():
    workflows = dict()
    ratings = list()

    onRatings = False

    for l in data:
        if l == "":
            onRatings = True
            continue

        if onRatings:
            t = l[1:-1].split(",")

            ex = ["x", "m", "a", "s"]

            rating = dict()

            for a in range(len(t)):
                b = int(t[a].split("=")[1])
                rating[ex[a]] = b

            ratings.append(rating)

        else:
            t = l.split("{")
            name = t[0]
            unparsedRules = t[1][:-1].split(",")

            parsedRules = list()

            for r in unparsedRules:
                t1 = r.split(":")
                if len(t1) == 1:
                    parsedRules.append((t1))
                else:
                    parsedRules.append((t1[0][0], t1[0][1], int(t1[0][2:]), t1[1]))

            workflows[name] = parsedRules.copy()

    # for x in workflows:
    #     print(workflows[x])

    # for x in ratings:
    #     print(x)

    return workflows, ratings


def processRating(workflows, rating, startWorkflow):
    if startWorkflow == "A":
        return True
    elif startWorkflow == "R":
        return False

    rules = workflows[startWorkflow]

    for rule in rules:
        # print("RULE: ", rule)
        if len(rule) == 1:
            if rule[0] == "A":
                return True
            elif rule[0] == "R":
                return False
            else:
                return processRating(workflows, rating, rule[0])
        else:
            category = rule[0]
            operation = rule[1]
            testValue = rule[2]
            possibleNextWorkflow = rule[3]

            # print(category)
            # print(operation)
            # print(testValue)
            # print(possibleNextWorkflow)
            # print(rating[category])

            if operation == "<":
                if rating[category] < testValue:
                    return processRating(workflows, rating, possibleNextWorkflow)
            elif operation == ">":
                if rating[category] > testValue:
                    return processRating(workflows, rating, possibleNextWorkflow)


def getWorkflowCount(workflowMap: dict, currentState: str, ranges: dict):
    # x, m, a, s = [z - y + 1 for y, z in ranges.values()]
    # print(f"{currentState} | {x * m * a * s}")
    if currentState == "A":
        x, m, a, s = [z - y + 1 for y, z in ranges.values()]
        return x * m * a * s
    elif currentState == "R":
        return 0
    else:
        rulesForState = workflowMap[currentState]

        totalCounts = 0

        currentRanges = ranges.copy()

        for rule in rulesForState:
            if len(rule) == 1:
                totalCounts += getWorkflowCount(workflowMap, rule[0], currentRanges)
            else:
                rangeTuple = currentRanges[rule[0]]

                rangesForTrue = currentRanges.copy()
                if rule[1] == "<":
                    rangesForTrue[rule[0]] = (
                        rangeTuple[0],
                        min(rangeTuple[1], rule[2]) - 1,
                    )
                    currentRanges[rule[0]] = (
                        max(rangeTuple[0], rule[2]),
                        rangeTuple[1],
                    )
                else:
                    rangesForTrue[rule[0]] = (
                        max(rangeTuple[0], rule[2]) + 1,
                        rangeTuple[1],
                    )
                    currentRanges[rule[0]] = (
                        rangeTuple[0],
                        min(rangeTuple[1], rule[2]),
                    )

                countForTrue = getWorkflowCount(workflowMap, rule[3], rangesForTrue)

                totalCounts += countForTrue

        return totalCounts


def pt1():
    workflows, ratings = getInput()

    ans = 0

    for r in ratings:
        if processRating(workflows, r, "in"):
            ans += sum(r.values())

    return ans


def pt2():
    workflows, _ = getInput()

    ans = getWorkflowCount(
        workflows,
        "in",
        {
            "x": (1, 4000),
            "m": (1, 4000),
            "a": (1, 4000),
            "s": (1, 4000),
        },
    )

    return ans


print("Part 1 Answer:")
start_time = time.time()
print(Fore.GREEN + str(pt1()))
print(Style.RESET_ALL, end="")
print(f"It took {time.time() - start_time}s to get answer")
start_time = time.time()
print()
print("Part 2 Answer:")
print(Fore.GREEN + str(pt2()))
print(Style.RESET_ALL, end="")
print(f"It took {time.time() - start_time}s to get answer")
