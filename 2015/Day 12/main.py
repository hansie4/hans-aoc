import os
import json

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read()


def getSum(ds):
    if "int" in str(type(ds)):
        return ds
    elif "NoneType" in str(type(ds)) or "str" in str(type(ds)):
        return 0
    elif "list" in str(type(ds)):
        sum = 0
        for x in ds:
            sum += getSum(x)
        return sum
    elif "dict" in str(type(ds)):
        sum = 0
        for x in ds.keys():
            sum += getSum(ds[x])
        return sum
    else:
        print(type(ds))


def getSum2(ds):
    if "int" in str(type(ds)):
        return ds
    elif "NoneType" in str(type(ds)) or "str" in str(type(ds)):
        return 0
    elif "list" in str(type(ds)):
        sum = 0
        for x in ds:
            sum += getSum(x)
        return sum
    elif "dict" in str(type(ds)):
        sum = 0

        print(ds.values())

        for x in ds.keys():
            sum += getSum(ds[x])
        return sum
    else:
        print(type(ds))


def pt1():
    info = json.loads(data)

    a = getSum(info)

    print(a)


def pt2():
    info = json.loads(data)

    a = getSum2(info)

    print(a)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
