import math

with open("input.txt", "r") as reader:
    Xa, Ya, Xb, Yb = map(int, reader.readline().split(" "))

# First case
r1 = math.sqrt(Xa**2 + Ya**2)
r2 = math.sqrt(Xb**2 + Yb**2)
dist_1 = r1 + r2

if r1 == 0 or r2 == 0:
    dist_2 = max(r1, r2)
elif Xa == Xb and Ya == Yb:
    dist_2 = 0
else:
    # Second case using atan2 for angle calculation
    angle_a = math.atan2(Ya, Xa)
    angle_b = math.atan2(Yb, Xb)

    angle_ab = angle_b - angle_a

    while angle_ab > math.pi:
        angle_ab -= 2 * math.pi
    while angle_ab < -math.pi:
        angle_ab += 2 * math.pi

    dist_2 = min(r1, r2) * abs(angle_ab) + abs(r1 - r2)

ans = min(dist_1, dist_2)

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))
