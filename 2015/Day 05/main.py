import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def isVowel(letter: str):
    if letter == "a":
        return True
    if letter == "e":
        return True
    if letter == "i":
        return True
    if letter == "o":
        return True
    if letter == "u":
        return True

    return False


def isNiceString1(test: str):
    vowelSet = set()
    vowelCount = 0
    doubleLetterCount = 0
    hasBadSubstring = False

    lastLetter = ""

    for l in test:
        if l not in vowelSet and isVowel(l):
            vowelSet.add(l)

        if isVowel(l):
            vowelCount += 1

        if lastLetter == l:
            doubleLetterCount += 1

        if l == "b" and lastLetter == "a":
            hasBadSubstring = True
            break
        if l == "d" and lastLetter == "c":
            hasBadSubstring = True
            break
        if l == "q" and lastLetter == "p":
            hasBadSubstring = True
            break
        if l == "y" and lastLetter == "x":
            hasBadSubstring = True
            break

        lastLetter = l

    if vowelCount < 3 or doubleLetterCount == 0 or hasBadSubstring:
        return False

    return True


def isNiceString2(test: str):
    twoOneApart = False
    threeInARows = 0

    for x in range(len(test) - 2):
        l1 = test[x]
        l2 = test[x + 1]
        l3 = test[x + 2]

        if l1 == l3 and l1 != l2:
            twoOneApart = True
        elif l1 == l2 == l3:
            threeInARows += 1

    duos = set()
    expected = len(test) - 1

    pairTestPass = False

    for x in range(len(test) - 1):
        ss = test[x : x + 2]

        duos.add(ss)

    if (expected - threeInARows) > len(duos):
        # print(test)
        pairTestPass = True

    if twoOneApart and pairTestPass:
        # print(test)
        return True

    return False


def pt1():
    niceStrings = 0

    for l in data:
        if isNiceString1(l):
            niceStrings += 1

    print(niceStrings)


def pt2():
    niceStrings = 0

    for l in data:
        if isNiceString2(l):
            niceStrings += 1

    print(niceStrings)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
