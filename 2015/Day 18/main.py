import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def removeIfExists(l: list, el: tuple):
    if el in l:
        l.remove(el)


def getNeigborsToCheck(board: list, x: int, y: int):
    neighborsToCheck = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]

    if x == 0:
        removeIfExists(neighborsToCheck, (-1, -1))
        removeIfExists(neighborsToCheck, (-1, 0))
        removeIfExists(neighborsToCheck, (-1, 1))

    if x == len(board[0]) - 1:
        removeIfExists(neighborsToCheck, (1, -1))
        removeIfExists(neighborsToCheck, (1, 0))
        removeIfExists(neighborsToCheck, (1, 1))

    if y == 0:
        removeIfExists(neighborsToCheck, (-1, -1))
        removeIfExists(neighborsToCheck, (0, -1))
        removeIfExists(neighborsToCheck, (1, -1))

    if y == len(board) - 1:
        removeIfExists(neighborsToCheck, (-1, 1))
        removeIfExists(neighborsToCheck, (0, 1))
        removeIfExists(neighborsToCheck, (1, 1))

    return neighborsToCheck


def getNeighborsOn(board: list, x: int, y: int):
    neighborsToCheck = getNeigborsToCheck(board, x, y)

    neighborsOn = 0

    for z in neighborsToCheck:
        if board[y + z[1]][x + z[0]] == "#":
            neighborsOn += 1

    return neighborsOn


def createNeightborBoard(board: list):
    neighborBoard = list()

    for y in range(len(board)):
        temp = list()
        for x in range(len(board[y])):
            temp.append(getNeighborsOn(board, x, y))
        neighborBoard.append(temp)

    return neighborBoard


def cloneBoard(info: list):
    board = list()

    for y in range(len(info)):
        temp = list()
        for x in range(len(info[y])):
            temp.append(info[y][x])

        board.append(temp)

    return board


def printBoard(board: list):
    for x in board:
        temp = list(map(lambda z: str(z), x))
        print("".join(temp))


def runSim(board: list):
    futureBoard = cloneBoard(board)

    nBoard = createNeightborBoard(futureBoard)

    for y in range(len(board)):
        for x in range(len(board[y])):
            isOn = board[y][x] == "#"
            neighbors = nBoard[y][x]

            if isOn:
                if neighbors == 2 or neighbors == 3:
                    futureBoard[y][x] = "#"
                else:
                    futureBoard[y][x] = "."
            else:
                if neighbors == 3:
                    futureBoard[y][x] = "#"
                else:
                    futureBoard[y][x] = "."

    return futureBoard


def countLightsOn(board: list):
    numLights = 0

    for y in board:
        for x in y:
            if x == "#":
                numLights += 1

    return numLights


def setCornerLightsOn(board: list):
    height = len(board)
    width = len(board[0])

    board[0][0] = "#"
    board[0][width - 1] = "#"
    board[height - 1][0] = "#"
    board[height - 1][width - 1] = "#"


def pt1():
    NUMBER_OF_RUNS = 100

    currentBoard = data

    # print("Initial state:")
    # printBoard(currentBoard)
    # print()

    tempBoard = cloneBoard(currentBoard)

    ans = 0

    for x in range(NUMBER_OF_RUNS):
        # print(f"After {x + 1} step:")
        tempBoard = runSim(tempBoard)
        # printBoard(tempBoard)
        ans = countLightsOn(tempBoard)
        # print(countLightsOn(tempBoard))
        # print()

    print(ans)


def pt2():
    NUMBER_OF_RUNS = 100

    currentBoard = data

    # print("Initial state:")
    # printBoard(currentBoard)
    # print()

    tempBoard = cloneBoard(currentBoard)

    ans = 0

    for x in range(NUMBER_OF_RUNS):
        # print(f"After {x + 1} step:")
        setCornerLightsOn(tempBoard)
        tempBoard = runSim(tempBoard)
        setCornerLightsOn(tempBoard)
        # printBoard(tempBoard)
        ans = countLightsOn(tempBoard)
        # print(ans)
        # print()

    print(ans)


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
