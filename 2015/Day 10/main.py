import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read()


def lookAndSay(val: str):
    cutUp = [""] * len(val)

    i = -1
    lastVal = ""
    for x in val:
        if x != lastVal:
            i += 1

        lastVal = x

        cutUp[i] = cutUp[i] + lastVal

    # print(cutUp)
    for x in range(len(cutUp)):
        if cutUp[x]:
            cutUp[x] = newString(cutUp[x])
    # print(cutUp)

    new = "".join(cutUp)
    # print(new)
    return new


def newString(val: str):
    ch = val[0]
    ln = len(val)
    return str(ln) + ch


def pt1():
    print(data)
    temp = data
    for x in range(50):
        print("Run: ", x + 1)
        temp = lookAndSay(temp)
        # print(temp)
    print(len(temp))

    # f = open(os.path.join(script_dir, "output.txt"), "w")
    # f.write(temp)
    # f.close()


def pt2():
    pass


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
