import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read()


def pt1():
    pass


def pt2():
    pass


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
