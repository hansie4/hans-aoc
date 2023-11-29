import os
import numpy

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def lineToData(line: str):
    temp1 = line.split(" ")

    if len(temp1) == 5:
        operation = temp1[1]
        temp2 = temp1[2].split(",")
        temp3 = temp1[4].split(",")

        x1 = int(temp2[0])
        y1 = int(temp2[1])
        x2 = int(temp3[0])
        y2 = int(temp3[1])
    else:
        operation = temp1[0]
        temp2 = temp1[1].split(",")
        temp3 = temp1[3].split(",")

        x1 = int(temp2[0])
        y1 = int(temp2[1])
        x2 = int(temp3[0])
        y2 = int(temp3[1])

    return (operation, x1, y1, x2, y2)


def performAction1(grid, op):
    for y in range(op[2], op[4] + 1):
        for x in range(op[1], op[3] + 1):
            if op[0] == "toggle":
                grid[y][x] = 0 if grid[y][x] == 1 else 1
            elif op[0] == "on":
                grid[y][x] = 1
            else:
                grid[y][x] = 0


def performAction2(grid, op):
    for y in range(op[2], op[4] + 1):
        for x in range(op[1], op[3] + 1):
            if op[0] == "toggle":
                grid[y][x] = grid[y][x] + 2
            elif op[0] == "on":
                grid[y][x] = grid[y][x] + 1
            else:
                grid[y][x] = grid[y][x] - 1 if grid[y][x] > 0 else 0


def pt1():
    grid = [[0 for y in range(1000)] for x in range(1000)]

    for line in data:
        performAction1(grid, lineToData(line))

    print(sum(sum(grid, [])))

    # numpy.savetxt("temp.txt", grid, fmt="%i", delimiter="")


def pt2():
    grid = [[0 for y in range(1000)] for x in range(1000)]

    for line in data:
        performAction2(grid, lineToData(line))

    print(sum(sum(grid, [])))

    numpy.savetxt("temp.txt", grid, fmt="%i", delimiter="")


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
