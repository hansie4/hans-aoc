import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read()

charMap = dict()


def setupCharMap():
    for x in range(97, 123):
        charMap[chr(x)] = x


def reverseStringToList(v: str):
    chars = [None] * len(v)
    for x in range(len(v)):
        chars[len(v) - x - 1] = v[x]
    return chars


def incrementString(v: str):
    # print(v)

    chars = reverseStringToList(v)

    done = False
    currentIndex = 0
    while not done:
        if chars[currentIndex] == "z":
            chars[currentIndex] = "a"
            currentIndex += 1
        else:
            chars[currentIndex] = chr(charMap[chars[currentIndex]] + 1)
            done = True

    chars = reverseStringToList(chars)

    # print(chars)
    return "".join(chars)


def validateString(v: str):
    if isBadLetter(v[0]) or isBadLetter(v[1]):
        return False

    has3Adj = False
    for x in range(len(v) - 2):
        v1 = v[x]
        v2 = v[x + 1]
        v3 = v[x + 2]

        if isBadLetter(v3):
            return False

        n1 = charMap[v1]
        n2 = charMap[v2]
        n3 = charMap[v3]

        if n1 + 1 == n2 and n2 + 1 == n3:
            has3Adj = True
            break

    if not has3Adj:
        return False

    pairs = set()
    wasLastPair = False
    for x in range(len(v) - 1):
        v1 = v[x]
        v2 = v[x + 1]

        if v1 == v2 and not wasLastPair:
            pairs.add("".join([v1, v2]))
            wasLastPair = True
        else:
            wasLastPair = False

        if len(pairs) >= 2:
            break

    if len(pairs) < 2:
        return False

    return True


def isBadLetter(c: str):
    return c in ["i", "o", "l"]


def pt1():
    password = data

    print(incrementString(password))

    done = False
    attempt = 1
    while not done:
        password = incrementString(password)
        t2 = validateString(password)

        if not t2 and attempt % 10 == 0:
            print("Attempt # {} | {}".format(attempt, password))

        if t2:
            print("Password Found in {} attempts: {}".format(attempt, password))
            done = True

        attempt += 1


def pt2():
    password = "vzbxxyzz"

    print(incrementString(password))

    done = False
    attempt = 1
    while not done:
        password = incrementString(password)
        t2 = validateString(password)

        if not t2 and attempt % 10 == 0:
            print("Attempt # {} | {}".format(attempt, password))

        if t2:
            print("Password Found in {} attempts: {}".format(attempt, password))
            done = True

        attempt += 1


setupCharMap()
print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
