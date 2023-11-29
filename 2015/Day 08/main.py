import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def pt1():
    total = 0

    for line in data:
        offset = -2

        t = line[1 : len(line) - 1]

        offset = offset - (t.count('\\"') * 1)
        t = t.replace('\\"', "")

        offset = offset - (t.count("\\\\") * 1)
        t = t.replace("\\\\", "")

        offset = offset - (t.count("\\x") * 3)
        t = t.replace("\\x", "")

        # print(
        #    line + " | " + t + " | " + str(len(line)) + " | " + str(len(line) + offset)
        # )

        total += offset * -1

    print(total)


def pt2():
    total = 0

    for line in data:
        offset = len(line)

        offset = offset + (line.count('"') * 1)

        offset = offset + (line.count("\\") * 1)

        total += offset + 2 - len(line)

    print(total)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
