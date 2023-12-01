import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input_test.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def replaceValues(k: str, reversed: bool):
    strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    x = k

    if reversed:
        x = k[::-1]
        for z in range(len(strings)):
            strings[z] = strings[z][::-1]

    # print(strings)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    indexes = [1000000] * len(strings)

    for s in range(len(strings)):
        try:
            indexes[s] = x.index(strings[s])
        except:
            indexes[s] = 1000000

    # print(indexes)

    firstIndex = indexes.index(min(indexes))

    newString = x.replace(strings[firstIndex], str(nums[firstIndex]), 1)

    if reversed:
        return newString[::-1]
    else:
        return newString


def pt1():
    values = list()
    for x in data:
        print("Checking ", x)

        v1 = None
        v2 = None
        p1 = 0
        p2 = len(x) - 1

        for y in range(len(x)):
            if x[p1].isdigit():
                v1 = int(x[p1])

            if x[p2].isdigit():
                v2 = int(x[p2])

            if v1 == None:
                p1 += 1
            if v2 == None:
                p2 -= 1

            if v1 and v2:
                break

        values.append((v1 * 10) + v2)

    print(sum(values))


def pt2():
    values = list()

    updatedData = data.copy()

    for x in range(len(updatedData)):
        a = replaceValues(x, False)
        b = replaceValues(a, True)
        updatedData[x] = b

    for x in updatedData:
        print(x)

    for x in updatedData:
        print("Checking ", x)

        v1 = None
        v2 = None
        p1 = 0
        p2 = len(x) - 1

        for y in range(len(x)):
            if x[p1].isdigit():
                v1 = int(x[p1])

            if x[p2].isdigit():
                v2 = int(x[p2])

            if v1 == None:
                p1 += 1
            if v2 == None:
                p2 -= 1

            if v1 and v2:
                break

        values.append((v1 * 10) + v2)

    print(sum(values))


print("Part 1 Answer:")
# pt1()
print("Part 2 Answer:")
pt2()
