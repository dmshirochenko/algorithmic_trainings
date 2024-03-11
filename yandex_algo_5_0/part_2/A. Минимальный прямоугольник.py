# Reading from the file
import math

with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    min_x, min_y = math.inf, math.inf
    max_x, max_y = -math.inf, -math.inf
    for i in range(N):
        x, y = map(int, reader.readline().strip().split(" "))
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)


# Writing to the file
with open("output.txt", "w") as file:
    ans = f"{min_x} {min_y} {max_x} {max_y}"
    file.write(ans)
