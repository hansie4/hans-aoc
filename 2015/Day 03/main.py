import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read()


def pt1():
    currentPos = (0, 0)
    positions = set(currentPos)

    for move in data:
        if move == ">":
            currentPos = (currentPos[0] + 1, currentPos[1])
        elif move == "<":
            currentPos = (currentPos[0] - 1, currentPos[1])
        elif move == "^":
            currentPos = (currentPos[0], currentPos[1] + 1)
        else:
            currentPos = (currentPos[0], currentPos[1] - 1)

        positions.add(currentPos)

    print(len(positions))


def pt2():
    santaPos = (0, 0)
    roboPos = (0, 0)
    tempPos = (0, 0)
    positions = set(santaPos)

    for x in range(len(data)):
        isSantaMove = x % 2 == 0

        move = data[x]

        # print("-------------------------")
        # print(positions)
        # print("Is Santa Move: ", isSantaMove)

        if move == ">":
            tempPos = (
                (santaPos[0] + 1, santaPos[1])
                if isSantaMove
                else (roboPos[0] + 1, roboPos[1])
            )
            # print("> NEW POS: ", tempPos)
        elif move == "<":
            tempPos = (
                (santaPos[0] - 1, santaPos[1])
                if isSantaMove
                else (roboPos[0] - 1, roboPos[1])
            )
            # print("< NEW POS: ", tempPos)
        elif move == "^":
            tempPos = (
                (santaPos[0], santaPos[1] + 1)
                if isSantaMove
                else (roboPos[0], roboPos[1] + 1)
            )
            # print("^ NEW POS: ", tempPos)
        else:
            tempPos = (
                (santaPos[0], santaPos[1] - 1)
                if isSantaMove
                else (roboPos[0], roboPos[1] - 1)
            )
            # print("v NEW POS: ", tempPos)

        if isSantaMove:
            santaPos = tempPos
            # print("SANTA POS: ", santaPos)
            positions.add(santaPos)
        else:
            roboPos = tempPos
            # print("ROBO POS: ", roboPos)
            positions.add(roboPos)

    # print(positions)
    print(len(positions))


print("Part 1 Answer:")
pt1()

print("Part 2 Answer:")
pt2()
