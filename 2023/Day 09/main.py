import os
import time

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def getProcessedData(info):
    processed = list()

    for x in info:
        t = x.split()

        for x in range(len(t)):
            t[x] = int(t[x])

        processed.append(t)

    return processed


def predictValue(values: list):
    # print(values)

    allZeros = True

    for x in values:
        if x != 0:
            allZeros = False
            break

    if allZeros:
        return 0

    diffs = list()

    for x in range(len(values) - 1):
        v1 = values[x]
        v2 = values[x + 1]

        diff = v2 - v1

        diffs.append(diff)

    pred = predictValue(diffs)

    # print(pred)
    return values[-1] + pred


def pt1():
    processedData = getProcessedData(data)

    acc = 0

    for x in processedData:
        pred = predictValue(x)
        acc += pred

    print(acc)
    return acc


def pt2():
    processedData = getProcessedData(data)

    acc = 0

    for x in processedData:
        pred = predictValue(x[::-1])
        acc += pred

    print(acc)
    return acc


print("Part 1 Answer:")
start_time = time.time()
pt1()
print(f"It took {time.time() - start_time}s to get answer")
start_time = time.time()
print("Part 2 Answer:")
pt2()
print(f"It took {time.time() - start_time}s to get answer")
