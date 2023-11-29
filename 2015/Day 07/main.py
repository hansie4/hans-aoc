import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def pt1():
    values = dict()
    instructions = list(map(lambda x: x.split(" "), data))
    nextInstructions = list()

    iteration = 1

    while len(instructions) > 0:
        # print("--------------------------")
        # print(
        #    "Iteration {} | # of instructions: {}".format(iteration, len(instructions))
        # )
        for line in instructions:
            if len(line) == 3:
                if line[0].isnumeric():
                    values[line[2]] = int(line[0])
                else:
                    if line[0] in values:
                        values[line[2]] = values[line[0]]
                    else:
                        nextInstructions.append(line)
            elif len(line) == 4:
                if line[1] in values:
                    values[line[3]] = 65535 - int(values[line[1]])
                else:
                    nextInstructions.append(line)
            else:
                canDo = True

                x1 = line[0]
                x2 = line[2]
                y1 = line[4]

                if x1.isnumeric():
                    x1 = int(x1)
                elif x1 in values:
                    x1 = values[x1]
                else:
                    canDo = False

                if x2.isnumeric():
                    x2 = int(x2)
                elif x2 in values:
                    x2 = values[x2]
                else:
                    canDo = False

                if canDo:
                    if line[1] == "AND":
                        values[y1] = x1 & x2
                    elif line[1] == "OR":
                        values[y1] = x1 | x2
                    elif line[1] == "LSHIFT":
                        values[y1] = x1 << x2
                    elif line[1] == "RSHIFT":
                        values[y1] = x1 >> x2
                else:
                    nextInstructions.append(line)

        # if x == 8:
        #     for a in nextInstructions:
        #         print(a)

        instructions = nextInstructions.copy()
        nextInstructions.clear()

        iteration += 1

    print(values["a"])
    return values["a"]


def pt2(part1answer):
    for x in range(len(data)):
        temp1 = data[x].split(" ")
        if len(temp1) == 3 and temp1[2] == "b":
            temp1[0] = str(part1answer)
            temp2 = " ".join(temp1)
            data[x] = temp2

    return pt1()


print("Part 1 Answer:")
a = pt1()
print("Part 2 Answer:")
pt2(a)
