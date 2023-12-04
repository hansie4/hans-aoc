import os
import math

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getLines(info: list):
    lines = list()

    for x in info:
        t = x.split(":", 2)
        id = int(t[0][5:])
        t = t[1].split("|", 2)

        lines.append((t[0].split(), t[1].split(), id))

    return lines


def pt1():
    lines = getLines(data)

    # print(lines)

    ans = 0

    for x in lines:
        matches = 0

        for y in x[0]:
            if y in x[1]:
                matches += 1

        # print(matches)
        if matches > 0:
            ans += int(math.pow(2, matches - 1))

    print(ans)
    return ans


def pt2():
    lines = getLines(data)

    # print(lines)

    matchDict = [0] * (len(lines) + 1)

    for x in lines:
        matches = 0

        for y in x[0]:
            if y in x[1]:
                matches += 1

        # print(matches)
        if matches > 0:
            matchDict[x[2]] = matches

    allCardsToProcess = list()

    for x in lines:
        allCardsToProcess.append(x[2])

    cardsToAddDict = dict()
    for x in lines:
        cardsToAddDict[x[2]] = [x + 1 for x in range(x[2], x[2] + matchDict[x[2]])]

    # print(cardsToAddDict)

    currentCard = 0
    endOfList = len(allCardsToProcess)
    allCardsToProcess.sort()

    while currentCard < endOfList:
        currentCardId = allCardsToProcess[currentCard]
        matchesForCard = matchDict[currentCardId]

        cardsToAdd = cardsToAddDict[currentCardId]

        for x in cardsToAdd:
            allCardsToProcess.append(x)

        endOfList = len(allCardsToProcess)
        # print("Size: ", endOfList)
        currentCard += 1

    # allCardsToProcess.sort()
    # print(allCardsToProcess)
    ans = len(allCardsToProcess)

    print(ans)
    return ans


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
