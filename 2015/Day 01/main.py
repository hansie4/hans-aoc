import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

steps = f.read()


def pt1():
    currentFloor = 0

    for x in steps:
        if x == "(":
            currentFloor += 1
        else:
            currentFloor -= 1

    print(currentFloor)


def pt2():
    currentFloor = 0
    currentChar = 1

    for x in steps:
        if x == "(":
            currentFloor += 1
        else:
            currentFloor -= 1

        if currentFloor == -1:
            print(currentChar)
            break

        currentChar += 1


print("Part 1 Answer:")
pt1()

print("Part 2 Answer:")
pt2()
