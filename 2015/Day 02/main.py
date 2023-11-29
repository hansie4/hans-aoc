import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
# rel_path = "input_temp.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()


def pt1():
    ans = 0

    for box in data:
        mes = box.split("x")

        l, w, h = int(mes[0]), int(mes[1]), int(mes[2])

        s1 = l * w
        s2 = w * h
        s3 = h * l

        smallest = min(s1, s2, s3)

        ans += (2 * s1) + (2 * s2) + (2 * s3) + smallest

    print(ans)


def pt2():
    ans = 0

    for box in data:
        mes = box.split("x")

        l, w, h = int(mes[0]), int(mes[1]), int(mes[2])

        m = max(l, w, h)

        rib = ((2 * l) + (2 * w) + (2 * h)) - (2 * m)

        vol = l * w * h

        ans += rib + vol

    print(ans)


print("Answer to pt 1:")
pt1()

print("Answer to pt 2:")
pt2()
