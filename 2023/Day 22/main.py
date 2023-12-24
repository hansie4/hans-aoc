import os
import time
from colorama import Fore, Style
import sys
from pprint import pprint

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def toListOfPoints(p1: tuple, p2: tuple):
    points = set()
    for x in range(p1[0], p2[0] + 1):
        for y in range(p1[1], p2[1] + 1):
            for z in range(p1[2], p2[2] + 1):
                points.add((x, y, z))
    return points


def readInBlocks():
    blocks = dict()

    for lI in range(len(data)):
        t = data[lI].split("~")
        p1 = tuple(map(lambda x: int(x), t[0].split(",")))
        p2 = tuple(map(lambda x: int(x), t[1].split(",")))
        points = toListOfPoints(p1, p2)

        # print(points)

        blocks[lI] = points

    return blocks


def getBounds(blocks: dict):
    minX = sys.maxsize
    maxX = -sys.maxsize
    minY = sys.maxsize
    maxY = -sys.maxsize
    minZ = sys.maxsize
    maxZ = -sys.maxsize

    for pointSet in blocks.values():
        for x, y, z in pointSet:
            if x < minX:
                minX = x
            if x > maxX:
                maxX = x
            if y < minY:
                minY = y
            if y > maxY:
                maxY = y
            if z < minZ:
                minZ = z
            if z > maxZ:
                maxZ = z

    return ((minX, maxX + 1), (minY, maxY + 1), (minZ, maxZ + 1))


def blocksToGrid(blocks: dict):
    bounds = getBounds(blocks)

    grid = [
        [["" for k in range(bounds[0][1])] for j in range(bounds[1][1])]
        for i in range(bounds[2][1])
    ]

    for block in blocks:
        blockPoints = blocks[block]

        for x, y, z in blockPoints:
            grid[z][y][x] = block + 1

    return grid


def printGridX(grid):
    print()
    c = grid[::-1]

    for z in range(len(c)):
        for x in range(len(c[z][0])):
            cl = []

            for k in range(len(c[z])):
                cl.append(c[z][k][x])

            char = ""

            for y in cl:
                if y != "":
                    char = y
                    break

            if char == "":
                print(".", end="")
            else:
                # print(chr(ord("@") + (int(char))), end="")
                print(chr(ord("@") + (int(char) % 26) + 1), end="")
        print()
    print()


def printGridY(grid):
    print()
    c = grid[::-1]

    for z in range(len(c)):
        for y in range(len(c[z])):
            cl = c[z][y]

            char = ""

            for x in cl:
                if x != "":
                    char = x
                    break

            if char == "":
                print(".", end="")
            else:
                # print(chr(ord("@") + int(char)), end="")
                print(chr(ord("@") + (int(char) % 26) + 1), end="")
        print()
    print()


def settleBlocks(grid: list):
    for z in range(len(grid)):
        blocksInLayer = set()
        for i in range(len(grid[z])):
            for k in grid[z][i]:
                if k != "":
                    blocksInLayer.add(k)

        # print(blocksInLayer)

        for bNum in blocksInLayer:
            pointSettleAmount = dict()

            for row in range(len(grid[z])):
                for col in range(len(grid[z][row])):
                    if grid[z][row][col] == bNum:
                        count = 0
                        zToCheck = z - 1

                        while zToCheck > 0 and grid[zToCheck][row][col] == "":
                            count += 1
                            zToCheck -= 1

                        pointSettleAmount[(col, row, z)] = count

            # print(f"Block-{bNum} settle offsets: {pointSettleAmount}")
            minOffset = min(pointSettleAmount.values())
            # print(f"Moving block {minOffset} spots down")

            # Now offset the points
            for x, y, z in pointSettleAmount.keys():
                if z - minOffset != z:
                    grid[z - minOffset][y][x] = bNum
                    grid[z][y][x] = ""


def getSupports(grid: list):
    supports = dict()

    for z in range(len(grid)):
        for y in range(len(grid[z])):
            for x in range(len(grid[z][y])):
                if grid[z][y][x] != "":
                    supports[grid[z][y][x]] = set()

    for z in range(len(grid)):
        for y in range(len(grid[z])):
            for x in range(len(grid[z][y])):
                if grid[z][y][x] != "":
                    supportSet = supports[grid[z][y][x]]

                    if (
                        z + 1 < len(grid)
                        and grid[z + 1][y][x] != ""
                        and grid[z + 1][y][x] != grid[z][y][x]
                    ):
                        supportSet.add(grid[z + 1][y][x])

                    supports[grid[z][y][x]] = supportSet

    return supports


def whatBlocksBreakByRemovingBlock(blockToRemove: int, supports: dict, removed: set()):
    blockIsSupporting = supports[blockToRemove]

    blocksOthersSupport = set()

    for s in supports:
        if s != blockToRemove and s not in removed:
            for p in supports[s]:
                if p in blockIsSupporting:
                    blocksOthersSupport.add(p)

    return blockIsSupporting.difference(blocksOthersSupport)


def getChainReactionDamage(blockToRemove: int, supports: dict, removed: set):
    z = whatBlocksBreakByRemovingBlock(blockToRemove, supports, removed)

    if len(z) == 0:
        return 0

    count = 0

    removed.add(blockToRemove)

    for b in z:
        count += getChainReactionDamage(b, supports, removed)
        removed.add(b)

    return len(z) + count


def pt1():
    blocks = readInBlocks()
    grid = blocksToGrid(blocks)

    # printGridX(grid)
    # printGridY(grid)

    settleBlocks(grid)

    # printGridX(grid)
    # printGridY(grid)

    supports = getSupports(grid)

    z = 0

    for x in supports:
        a = whatBlocksBreakByRemovingBlock(x, supports, {})
        if len(a) == 0:
            z += 1

    return z


def pt2():
    blocks = readInBlocks()
    grid = blocksToGrid(blocks)

    settleBlocks(grid)

    supports = getSupports(grid)

    z = 0

    for b in supports.keys():
        r = set()
        a = getChainReactionDamage(b, supports, r)

        # print(f"{b} -> {a}")

        z += a

    return z


print("Part 1 Answer:")
start_time = time.time()
print(Fore.GREEN + str(pt1()))
print(Style.RESET_ALL, end="")
print(f"It took {time.time() - start_time}s to get answer")
start_time = time.time()
print()
print("Part 2 Answer:")
print(Fore.GREEN + str(pt2()))
print(Style.RESET_ALL, end="")
print(f"It took {time.time() - start_time}s to get answer")
