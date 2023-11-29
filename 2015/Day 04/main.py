import os
import hashlib

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.readline().strip()


def pt1():
    start = 0
    hashfound = False

    while not hashfound:
        val = "iwrupvqb" + str(start)

        # print(val)

        hash = hashlib.md5(val.encode()).hexdigest()

        # print(hash)

        if hash.startswith("00000"):
            print(hash)
            print(start)
            hashfound = True

        start += 1


def pt2():
    start = 0
    hashfound = False

    while not hashfound:
        val = "iwrupvqb" + str(start)

        # print(val)

        hash = hashlib.md5(val.encode()).hexdigest()

        # print(hash)

        if hash.startswith("000000"):
            print(hash)
            print(start)
            hashfound = True

        start += 1


print("Part 1 Answer: ")
pt1()
print("Part 2 Answer: ")
pt2()
