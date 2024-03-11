import math

# Reading from the file
with open("input.txt", "r") as reader:
    L, x1, v1, x2, v2 = map(int, reader.readline().strip().split(" "))


def calculate_meeting_time(R, x1, x2, v1, v2):
    if x1 == x2:
        return 0
    elif v1 == v2 == 0:
        return None
    elif v1 == -v2 and v2 > 0:
        t1 = abs(x2 - x1) / (2 * abs(v1))
        return t1
    elif v2 == -v1 and v1 > 0:
        t2 = (L - abs(x2 - x1)) / (2 * abs(v1))
        return t2
    elif v1 == v2:
        tmin = math.inf
        t1 = (x1 + (x2 - x1) / 2) / abs(v1)
        t2 = (L - (x1 + x2)) / (v1 + v2)
        if t1 > 0:
            tmin = min(tmin, t1)
        if t2 > 0:
            tmin = min(tmin, t2)
        return tmin
    else:
        tmin = math.inf
        for n in range(-100, 101):
            t1 = (L * n - (x1 + x2)) / (v1 + v2)
            t2 = (L * n - (x1 - x2)) / (v1 - v2)
            if t1 > 0:
                tmin = min(tmin, t1)
            if t2 > 0:
                tmin = min(tmin, t2)
        return tmin


ans = calculate_meeting_time(L, x1, x2, v1, v2)
# print('Ans ', ans)
# Writing to the file
with open("output.txt", "w") as file:
    if ans is not None:
        file.write("YES\n")
        file.write(str(ans))
    else:
        file.write("NO")
